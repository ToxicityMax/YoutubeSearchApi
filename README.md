## Youtube Search Api for Fampay Assingment
### Documented apis at /swagger and /redoc
#### Steps to run the project

1. Change directory to ./src and create env files

```bash
cd ./src
touch env.py docker.env
 ```

2. Take env.sample.py as reference for env.py

```python
DEBUG = True / False
SECRET = "anysecretkey"
GOOGLE_API_KEYS = ["key1", "key2"]
DATABASE = "postgres"
KEYWORD = "music"  # Keyword to make request to youtube
DB_USER = "db_user"
DB_NAME = "db_name"
DB_PASSWORD = "db_password"
DB_HOST = "db_host"
DB_PORT = "db_port"
CELERY_BROKER_URL = "url"
CELERY_RESULT_BACKEND = "url2"
```

3. docker.env vars

```bash
DATABASE=postgres
SQL_HOST=db
SQL_PORT=port
POSTGRES_USER=user
POSTGRES_PASSWORD=pass
POSTGRES_DB=db_name
DJANGO_SETTINGS_MODULE=fampay.settings
 ```

4. Final step is to create docker build and run services

```bash
cd <project_root>
docker-compose build
docker-compose run
```

### Access Swagger or redoc documentation at localhost/swagger or localhost/redoc 