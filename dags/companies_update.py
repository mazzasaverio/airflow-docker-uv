import pandas as pd
import duckdb
from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "start_date": datetime(2025, 5, 4),
}


@dag(
    dag_id="process_companies",
    default_args=default_args,
    schedule=None,
    catchup=False,
    tags=["duckdb", "companies"],
)
def process_companies_dag():
    @task
    def update_companies_table():
        file_path = "include/config/companies.csv"
        df = pd.read_csv(file_path)
        df.drop_duplicates(inplace=True)
        df["name"] = df["name"].str.lower()
        df["url"] = df["url"].str.rstrip("/")
        con = duckdb.connect("include/job_listings.db")
        df.to_sql("companies", con, if_exists="replace", index=False)
        con.close()

    @task
    def count_companies():
        con = duckdb.connect("include/job_listings.db")
        result = con.execute("SELECT COUNT(*) FROM companies;").fetchone()
        count = result
        print(f"Number of records in the companies table: {count}")
        con.close()

    update_companies_table() >> count_companies()


process_companies_dag()
