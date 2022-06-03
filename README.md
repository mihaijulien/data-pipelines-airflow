# ETL and Data Pipelines with Shell, Airflow and Kafka


![logo](https://user-images.githubusercontent.com/16778468/171870562-691553a6-6f9c-4c11-82e7-c021adb10be0.png)

**Course Link:**\
https://www.coursera.org/learn/etl-and-data-pipelines-shell-airflow-kafka

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

# Project

## Scenario
You are a data engineer at a data analytics consulting company. You have been assigned to a project that aims to de-congest the national highways by analyzing the road traffic data from different toll plazas. Each highway is operated by a different toll operator with a different IT setup that uses different file formats. Your job is to collect data available in different formats and consolidate it into a single file.

## Objectives
In this assignment you will author an Apache Airflow DAG that will:

Extract data from a csv file
Extract data from a tsv file
Extract data from a fixed width file
Transform the data
Load the transformed data into the staging area