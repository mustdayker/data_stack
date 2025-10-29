# Операции над данными для Дата-Инженера

## 1. Сбор и прием данных (Data Ingestion)
- Пакетная загрузка (Batch)
  - Полная выгрузка (Full Load)
  - Инкрементальная загрузка (Incremental/Delta Load)
- Потоковая загрузка (Streaming)
  - Чтение из Kafka/Kinesis/Pulsar
  - Запись в Data Lake/OLAP
- Change Data Capture (CDC)
  - На основе логов
  - На основе триггеров
  - По временным меткам
- Извлечение из API
  - REST API вызовы
  - Обработка пагинации
  - Аутентификация
  - Парсинг JSON/XML
- Веб-скрапинг

## 2. Преобразование и обработка (Data Transformation)
- Очистка данных
  - Обработка NULL-значений
  - Стандартизация форматов
  - Дедубликация
  - Валидация данных
- Обогащение данных
  - Джойны (JOIN)
  - Аггрегация (SUM, AVG, COUNT)
  - Добавление вычисляемых полей
- Трансформация структур
  - Pivot/Unpivot
  - Нормализация (1NF, 2NF, 3NF)
  - Денормализация
  - Парсинг JSON/XML/Avro
- Оконные функции
  - ROW_NUMBER(), RANK()
  - LAG(), LEAD()
  - Скользящие средние

## 3. Хранение и управление (Data Storage & Management)
- Операции с файлами
  - Партиционирование
  - Кластеризация/Сортировка
- Операции в СУБД
  - CRUD операции
  - Массовые операции (Bulk)
- Управление схемой
  - Schema-on-Write
  - Schema-on-Read
- Жизненный цикл данных
  - Архивация
  - TTL (Time to Live)
- Представления (Views)

## 4. Качество и надежность (Data Quality & Reliability)
- Проверки качества данных
  - Полнота (не NULL)
  - Уникальность
  - Достоверность
  - Согласованность
- Отказоустойчивые пайплайны
  - Логика повторов (Retry)
  - Идемпотентность
- Ведение версий данных
  - Delta Lake / Apache Iceberg
  - Time Travel

## 5. Оркестрация и планирование (Orchestration)
- Зависимости задач
- Планирование запуска
  - По расписанию
  - По событию
- Обработка ошибок
  - Оповещения (Email/Slack)
  - Мониторинг

## Ключевые технологии
- Языки программирования
  - SQL
  - Python
    - Pandas
    - PySpark
    - API-requests
  - Bash
- Фреймворки обработки
  - Apache Spark
  - dbt (data build tool)
- Системы хранения
  - PostgreSQL
  - Data Warehouses
    - BigQuery
    - Snowflake
    - Redshift
  - Data Lakes
    - S3/GCS
    - Parquet/Delta/Iceberg
- Оркестраторы
  - Apache Airflow
  - Prefect
  - Dagster