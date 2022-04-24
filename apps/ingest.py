from typing import Any

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, unix_timestamp, to_date

def init_spark():
  sql = SparkSession.builder\
    .appName("trip-app")\
    .config("spark.jars", "/opt/spark-apps/postgresql-42.2.22.jar")\
    .getOrCreate()
  sc = sql.sparkContext
  return sql,sc

def extract(sql, tables):
    dataframes = {}
    for table in tables:
        file_dir = "/opt/spark-data/{}.csv".format(table)
        dataframes[table] = sql.read.load(file_dir,format = "csv", inferSchema="true", sep=",", header="true") 
    return dataframes

def transform(dataframes):
    dataframes["course_attendance"] = dataframes["course_attendance"].withColumn('ATTEND_DT',to_date(unix_timestamp(col('ATTEND_DT'), 'dd-MMM-yy').cast("timestamp")))
    dataframes["enrollment"] = dataframes["enrollment"].withColumn('ENROLL_DT',to_date(unix_timestamp(col('ENROLL_DT'), 'dd-MMM-yy').cast("timestamp")))
    dataframes["schedule"] = dataframes["schedule"].withColumn('START_DT',to_date(unix_timestamp(col('START_DT'), 'dd-MMM-yy').cast("timestamp")))
    dataframes["schedule"] = dataframes["schedule"].withColumn('END_DT',to_date(unix_timestamp(col('END_DT'), 'dd-MMM-yy').cast("timestamp")))
    return dataframes

def load(dataframes, tables, url, properties):
    for table in tables:
        dataframes[table].write.jdbc(url=url, table="{}s".format(table), mode='append', properties=properties)

def main():
    url = "jdbc:postgresql://demo-database:5432/agriaku_university"
    properties = {
        "user": "postgres",
        "password": "test",
        "driver": "org.postgresql.Driver"
    }
    tables = [
        "course_attendance",
        "course",
        "enrollment",
        "schedule"
    ]
    sql,sc = init_spark()
    dataframes = extract(sql, tables)
    dataframes = transform(dataframes)
    load(dataframes, tables, url, properties)

if __name__ == '__main__':
  main()



