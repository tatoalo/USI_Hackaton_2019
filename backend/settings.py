import os

BACKEND_SETTINGS = {
    "elastic_host": os.environ["ELASTIC_HOST"],
    "elastic_username": os.environ["ELASTIC_USERNAME"],
    "elastic_password": os.environ["ELASTIC_PASSWORD"],
    "database_url": os.environ["DATABASE_URL"],
}
