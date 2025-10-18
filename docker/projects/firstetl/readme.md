# Команды для запуска:

```bash
# 2. Создаем папки для данных
mkdir -p airflow/dags airflow/logs airflow/plugins jupyter/notebooks superset/data

# 3. Запускаем все сервисы
docker compose up -d
docker compose down

# 5. Инициализируем Superset
docker compose exec superset superset db upgrade
docker compose exec superset superset fab create-admin --username admin --firstname Admin --lastname User --email admin@example.com --password admin
docker compose exec superset superset init

# Доп команды

# Удалить Noname контейнеры
docker volume prune
```

# Доступ к сервисам:
- Airflow: http://localhost:8080 (admin/admin)
- Jupyter: http://localhost:8888 (пароль: dataengineer)
- Superset: http://localhost:8088 (admin/admin)
- PostgreSQL: localhost:5432 (airflow/airflow)

Этот вариант использует готовый образ amancevice/superset:latest, в котором уже установлены все необходимые драйверы для PostgreSQL. Должно работать без проблем!
