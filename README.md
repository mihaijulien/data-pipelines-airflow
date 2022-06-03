# Data Pipelines with Airflow

## Initialise teh Airflow Database

Start the `airflow-init` container:

```sh
$ docker-compose up airflow-init
```

This service will essentially run `airflow db init` and create the admin user for the Airflow Database. By default, the account created has the login `airflow` and the password `airflow`.

## Start Airflow services

```sh
$ docker-compose up
```

## Access Airflow UI

Go to `localhost:8080`