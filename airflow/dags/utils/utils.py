from airflow.hooks.postgres_hook import PostgresHook
from datetime import timedelta
import ast


class Utils():
    CONNECTION = "my_prod_db_1"

    @staticmethod
    def get_params(base_name):

        postgres_hook = PostgresHook(postgres_conn_id=Utils.CONNECTION)
        records = postgres_hook.get_records(
            sql=f"select params_airflow from sources_captureparameters where name_base='{base_name}';",)
        return ast.literal_eval(records[0][0])

    @staticmethod
    def transform_interval(dict_interval):

        if dict_interval['type'] == "hour":
            return timedelta(hours=dict_interval["value"])
        elif dict_interval['type'] == "minute":
            return timedelta(minutes=dict_interval["value"])
        elif dict_interval['type'] == "second":
            return timedelta(seconds=dict_interval["value"])
        elif dict_interval['type'] == "cron":
            return dict_interval["value"]
        elif dict_interval['type'] == "text":
            return dict_interval["value"]
    
    @staticmethod
    def get_files_insert(base_name):
        postgres_hook = PostgresHook(postgres_conn_id=Utils.CONNECTION)
        records = postgres_hook.get_records(
            sql=f"select file_path from sources_fileprocessed where file_path like'%{base_name}%' and step_file='I' and status_file='R';",)
        return records        
