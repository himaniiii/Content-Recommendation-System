# database_utils.py
import mysql.connector

DB_CONFIG_GLOBAL = {
    'user': 'root',
    'password': 'Himani@12',
    'host': 'localhost',
    'database': 'global_data',
    'raise_on_warnings': True
}

DB_CONFIG_LOCAL = {
    'user': 'root',
    'password': 'Himani@12',
    'host': 'localhost',
    'database': 'iia',
    'raise_on_warnings': True
}

GLOBAL_TABLES = ['Social_Media_Info', 'Movie_TV_Data', 'Series_Info']
LOCAL_TABLES = ['action_series', 'animation_series', 'adventure_series', 'tv', 'imdb_movie_data', 'instagram', 'youtube']

def run_query(query, table_name):
    db_config = DB_CONFIG_GLOBAL if table_name in GLOBAL_TABLES else DB_CONFIG_LOCAL
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = cursor.column_names
    cursor.close()
    connection.close()
    return data, column_names
