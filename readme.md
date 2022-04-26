# Agriaku Take Home Test

## Tech

The tech used on this project:

- PostgreSQL
- Python 3.9
- Docker
- PySpark

## Setup

This project requires Docker, Docker Compose, and Java 11.

Build the project by execute:

```sh
sudo make build-images
```

To start the project, execute:
```sh
sudo make start-images
```

To Execute the ingestion, execute:
```sh
sudo make execute-ingestion
```

stop-images the project, execute:
```sh
sudo make stop-airflow
```

To remove the project, execute:
```sh
sudo drop drop-images
```

## Insight

This project wants to ingest from several table to Data Mart. The table is about Attendance from university courses and the insight that the stakeholder wants is weekly attendance percentage from the courses.