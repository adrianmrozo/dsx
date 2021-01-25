host = "postgres"
database = "milestone5"
port = "5432"
user = "postgres"
password = "pgpass"

import psycopg2
import numpy as np



con = psycopg2.connect(dbname=database, user=user, password=password, host=host, port = port)

cur = con.cursor()

#cur.execute("CREATE TABLE input_data (ID SERIAL PRIMARY KEY, input_label varchar);")
cur.execute("CREATE TABLE predictions (ID SERIAL PRIMARY KEY, prediction varchar);")

#cur.execute('''
#CREATE SEQUENCE idsequence
#    start 10
#    increment 1;''')

#commit data to db
con.commit()
con.close()

#store prediction 

def savingtestresult(pred_label):
#def savingtestresult(test_label, test_data, pred_label):

    host = "postgres"
    database = "milestone5"
    port = "5432"
    user = "postgres"
    password = "pgpass"

    con = psycopg2.connect(dbname=database, user=user, password=password, host=host, port = port)

    cur = con.cursor()
    savingtestresult.counter += 1
    
    #load prediction into database 
    #cur.execute("insert into predictions (ID, prediction) values (nextval('idsequence'), %s)", (pred_label,))
    cur.execute("insert into predictions (ID, prediction) values (%s, %s)", (savingtestresult.counter, pred_label))
    con.commit()
    con.close()

    
def printdatabase():
    import psycopg2 as pg
    #import pandas as pd
    #import pandas.io.sql as psql
    host = "postgres"
    database = "milestone5"
    port = "5432"
    user = "postgres"
    password = "pgpass"

    con = psycopg2.connect(dbname=database, user=user, password=password, host=host, port = port)

    cur = con.cursor()
    #record = pd.read_sql_table('table_name', connection)
    #record = pd.read_sql('select * from predictions', con)
    cur.execute("SELECT * from predictions")
    record = cur.fetchall()
    #another_attempt= psql.read_sql("SELECT * FROM input_data", con)

    return record

    con.close()


