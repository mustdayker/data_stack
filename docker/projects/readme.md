## Дата-стенд `etl_project_v1`

### 🗄️ Хранилище данных:
- `PostgreSQL` - основная БД для Airflow и Superset
- `MinIO` - объектное хранилище (аналог S3)

### ⚙️ Оркестрация данных:
- `Airflow` - платформа для оркестрации ETL/ELT процессов
- `Spark` - распределенная обработка данных (мастер + 2 воркера)

### 📊 Аналитика и визуализация:
- `Jupyter` - интерактивная разработка ноутбуков
- `Superset` - BI-платформа для дашбордов и аналитики

### 📈 Мониторинг:
- `Prometheus` - сбор и хранение метрик
- `Grafana` - визуализация метрик и дашборды
- `Node Exporter` - метрики системы
- `cAdvisor` - мониторинг контейнеров
- `StatsD Exporter` - преобразование метрик Airflow для Prometheus

## Пет проекты

- [`pet_01_flights.md`](pet_01_flights.md) - ETL-пайплайн анализа авиаперелётов в США

## Где брать датасеты

- [`https://www.kaggle.com/datasets`](https://www.kaggle.com/datasets)
- [`https://catalog.data.gov/dataset`](https://catalog.data.gov/dataset/)