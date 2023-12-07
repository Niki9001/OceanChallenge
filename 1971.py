import pandas as pd
import pymysql
import seaborn as sns
import matplotlib.pyplot as plt

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '238978',
    port = 3306,
    db = 'ocean'
)
cursor = connection.cursor()

query1 = """SELECT
    m.scientificName,
    m.scientificNameID,
    o.year,
    o.month,
    o.day,
    o.decimalLatitude,
    o.decimalLongitude,
    t.value as temperature 
FROM
    `mpo_nafo_bottomtrawl_occurrence_1970-2019` AS m
LEFT JOIN
    ocean.`mpo_nafo_bottomtrawl_event_1970-2019` AS o ON m.eventID = o.eventID
LEFT JOIN
    transformed_data AS t ON DATE(CONCAT(o.year, '-', LPAD(o.month, 2, '0'), '-', LPAD(o.day, 2, '0'))) = t.date;"""
cursor.execute(query1)

###############
df = pd.read_sql_query(query1,connection)
df.to_csv('occ by time and location and temp.csv')
