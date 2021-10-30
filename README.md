# About

Simple API using [Flask](https://flask.palletsprojects.com/en/2.0.x/).

# Requirements

* Python >= 3.9
* Poetry >= 1.1
* Direnv
* Linux/Mac


# Clone

```shell
git clone https://github.com/williamcanin/api-flask-restful.git
cd api-flask-restful
```


# Configuration

1 - Create database in PostGreSQL:

```shell
sudo -i -u postgres psql
postgres=# CREATE DATABASE "<DB_NAME>";
postgres=# \q
```

2 - Install dependencies:

```shell
poetry shell
poetry install
```

3 - Set variables environment:

```shell
echo "export FLASK_APP=manage:app" >> .envrc
echo "export FLASK_ENV=development" >> .envrc
echo "export DATABASE_URL=postgresql://postgres:<PASSWORD>@localhost:5432/<DB_NAME>" >> .envrc
echo "export SECRET_KEY=\"<YOUR_SECRET_KEY>\"" >> .envrc
```

4 - Permission enable for variables environment:

```shell
direnv allow .
```

5 - Migrate and Upgrade models for database:

```shell
flask db init
flask db migrate
flask db upgrade
```

6 - Create superuser:

```shell
flask createsuperuser
```

# Using:

1 - Run API:

```shell
flask run
```

Using the [Insomnia](https://insomnia.rest/download) or [Postman](https://www.postman.com/) for manipulation routes.

---
(c) William Canin - 2021
