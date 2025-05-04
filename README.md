Installare astro CLI

curl -sSL install.astronomer.io | sudo bash -s

# From your project root on your host machine:
sudo chown -R 50000:0 include
sudo chmod -R u+rw include


Backfill

airlflow dags backfill -s <start> -e <end> dag_id


TODO: chiedi nel gruppo reddit altre best practice data engineer airflow

Some best practice with airflow:
 - chiama il dag con lo stesso nome del file
 - setta catchup su false perchè nella maggior parte delle volte non è true il comportamento che si vuole e meglio controllare questo parametro
 - attenzione a sviluppare i task in modo che siano idempotent


sudo chown $USER:$USER include/job_listings.db
 chmod 644  include/job_listings.db   

 Per visualizzare la ui
duckdb -ui include/job_listings.db