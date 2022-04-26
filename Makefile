build-images:
	docker build -t cluster-apache-spark:3.0.2 .

start-images:
	docker-compose up -d

stop-images:
	docker-compose down

drop-images:
	docker-compose down -v || true
	docker-compose rm -f

execute-ingestion:
	docker exec agriaku-test_spark-worker-a_1 /opt/spark/bin/spark-submit --master spark://spark-master:7077 --jars /opt/spark-apps/postgresql-42.2.22.jar --driver-memory 1G --executor-memory 1G /opt/spark-apps/ingest.py