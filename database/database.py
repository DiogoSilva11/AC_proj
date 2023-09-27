import os
import pandas as pd
import sqlite3

db_file = 'basketball.db'
csv_folder_path = '../basketballPlayoffs'
csv_files = [
    'awards_players.csv',
    'coaches.csv',
    'players_teams.csv',
    'players.csv',
    'series_post.csv',
    'teams_post.csv',
    'teams.csv'
]

conn = sqlite3.connect(db_file)

for csv_file in csv_files:
    table_name = os.path.splitext(csv_file)[0] 
    csv_file_path = os.path.join(csv_folder_path, csv_file)
    df = pd.read_csv(csv_file_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)

conn.commit()
conn.close()

'''

# HOW TO QUERY DATABASE

import sqlite3

conn = sqlite3.connect('../database/basketball.db')
cursor = conn.cursor()
query = "select * from your_table_name;"  # replace table name
cursor.execute(query)

results = cursor.fetchall()
for row in results:
    print(row)

cursor.close()
conn.close()

'''
