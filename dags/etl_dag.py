from datetime import date, timedelta
from airflow import DAG

from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


default_ars = {
	'owner': 'Julien Mihai',
	'start_date': date.today().isoformat(),
	'email': 'dummy@dummy.com',
	'emailOnFailure': True,
	'emailOnRetry': True,
	'retries': 1,
	'retry_delay': timedelta(minutes=1)
}

#dag def
dag = DAG('ETL_toll_data',
	default_args = default_args,
	description = 'Apache Airflow Final Assignment',
	schedule_interval = timedelta(days=1))

#tasks

unzip_data = BashOperator(
    task_id = 'unzip_data',
    bash_command = 'wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz; gunzip -c tolldata.tgz | tar xvf -',
    dag = dag,
)

extract_data_from_csv = PythonOperator(
	task_id = 'extract_data_from_csv',
	python_callable = extract_data_from_csv_func('vehicle-data.csv', 'csv_data.csv'),
	dag=dag
	)

extract_data_from_tsv = PythonOperator(
    task_id = 'extract_data_from_tsv',
	python_callable = extract_data_from_csv_func('tollplaza-data.tsv', 'tsv_data.csv'),
	dag=dag
	)


def extract_data_from_csv_func(src_file, dest_file):
	vehicle_data = open(src_file, 'r')
	csv_data = open(dest_file, 'w')
	for line in vehicle_data:
		data = line.split(',')
		for i in data[:4]:
			csv_data.write(d)
	vehicle_data.close()
	csv_data.close()

# pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv
