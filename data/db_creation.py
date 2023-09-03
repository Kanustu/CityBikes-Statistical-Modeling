import sqlite3
from sqlite3 import Error
import pandas as pd
station_poi_df = pd.read_csv('/Users/jordankanius/Downloads/station_poi_df')
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection
def execute_query(connection, query,params=None):
    cursor = connection.cursor()
    try:
        if params is None:
            cursor.execute(query)
        else:
            cursor.execute(query, params)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
        
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
connection = create_connection('station_info.db')

create_table_stations = '''
CREATE TABLE stations(
address VARCHAR(50) PRIMARY KEY,
free_bikes INTEGER)
'''
create_poi_table = '''
CREATE TABLE IF NOT EXISTS poi_info(
address VARCHAR(50),
poi_name VARCHAR(50),
poi_address VARCHAR(50),
hours VARCHAR(50),
CONSTRAINT fk_poi_info FOREIGN KEY (address) REFERENCES stations(address))
'''

create_poi_metrics = '''
CREATE TABLE IF NOT EXISTS poi_metrics(
address VARCHAR(50) UNIQUE,
rating FLOAT,
popularity FLOAT,
CONSTRAINT fk_poi_metrics FOREIGN KEY (address) REFERENCES poi_info(poi_address))
'''
execute_query(connection, create_table_stations)
execute_query(connection, create_poi_table)
execute_query(connection, create_poi_metrics)

station_entry = []
station_table = station_poi_df[['station_address' ,'free_bikes']].drop_duplicates()
for x in range(len(station_table)):
    dict = {
    'address' : station_table['station_address'].to_list()[x],
    'free_bikes': station_table['free_bikes'].to_list()[x]
    }
    station_entry.append(dict)

poi_entry = []
poi_table = station_poi_df[['station_address','poi_name', 'address', 'hours']]
for x in range(len(poi_table)):
    dict = {
    'address':poi_table['station_address'].to_list()[x],
    'poi_name': poi_table['poi_name'].to_list()[x],
    'poi_address': poi_table['address'].to_list()[x],
    'hours': poi_table['hours'].to_list()[x]
    }
    poi_entry.append(dict)
poi_entry

metrics_entry = []   
poi_metrics = station_poi_df[['address', 'rating','popularity(0-1)']].drop_duplicates()
for x in range(len(poi_metrics)):
    dict ={
           'address':poi_metrics['address'].to_list()[x],
           'rating':poi_metrics['rating'].to_list()[x],
           'popularity':poi_metrics['popularity(0-1)'].to_list()[x]
          }
    metrics_entry.append(dict)

for entry in station_entry:
    execute_query(connection, "INSERT INTO stations (address, free_bikes) VALUES(?,?)",
                                (entry['address'], entry['free_bikes']))

for entry in poi_entry:
    execute_query(connection, "INSERT or REPLACE INTO poi_info (address,poi_name, poi_address, hours) VALUES(?,?,?,?)",
                                (entry['address'], entry['poi_name'], entry['poi_address'], entry['hours']))

for entry in metrics_entry:
    execute_query(connection, "INSERT INTO poi_metrics ( address, rating, popularity) VALUES(?,?,?)",
                                (entry['address'], entry['rating'], entry['popularity']))
    
