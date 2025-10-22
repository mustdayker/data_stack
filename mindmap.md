---
title: Стек дата-инженера
markmap:
  colorFreezeLevel: 2
  maxWidth: 250
---

https://markmap.js.org/

## Ядро (обязательно)

- Языки и инструменты
  - `Python`
  - `SQL`
  - `Bash`
- Git и основы DevOps
  - `Git`
  - `Linux CLI`
- Работа с данными
  - `ETL vs ELT`
  - `Моделирование: звезда, снежинка`
  - `CSV`
  - `JSON`
  - `Parquet`
  - `ORC`
  - `Avro`
- СУБД
  - `PostgreSQL`
  - `MySQL`
  - `DuckDB`
  - `ClickHouse`

## Обработка данных

### Batch (пакетная)
- Apache Spark
  - `local[*]`
  - `Кластер в Docker`
  - `partitioning`
  - `broadcast joins`
- Оркестрация
  - `Airflow`
  - `Prefect`
  - `Dagster`

### Streaming (потоковая)
- `Kafka`
- `Redpanda`
- `Spark Structured Streaming`
- `Flink`

## Хранилище и Data Lake

- Объектное хранилище
  - `MinIO`
  - `AWS S3`
  - `GCS`
- Таблицы нового поколения
  - `Delta Lake`
  - `Apache Iceberg`
  - `Apache Hudi`
- Архитектура
  - `Lakehouse`

## Инфраструктура

- Контейнеризация
  - `Docker`
  - `docker-compose.yml`
  - `Портабельность`
- Мониторинг
  - `Prometheus`
  - `Grafana`
  - `Экспорт метрик`
- IaC (опционально)
  - `Terraform`
- Логирование
  - `Loki`
  - `Grafana`
  - `ELK`

## Облачные платформы (по желанию)

- AWS
  - `Glue`
  - `S3`
  - `Redshift`
  - `MSK`
- GCP
  - `BigQuery`
  - `Dataflow`
  - `Pub/Sub`
- Azure
  - `Synapse`
  - `ADLS`
  - `Event Hubs`

## Инструменты для качества и ML

- `dbt`
- `Great Expectations`
- `Soda Core`
- `MLflow`
- `DVC`
- `Jupyter Notebook`