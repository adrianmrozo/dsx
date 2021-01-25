#host = "127.0.0.1"
#database = "milestone5"
#port = "5005"
#user = input("Insert a name for your database:") or "postgres"
#password = input("Insert a password for your database:") or "pgpass"


host = "postgres"
database = "milestone5"
port = "5432"
user = "postgres"
password = "pgpass"

import psycopg2
import numpy as np



con = psycopg2.connect(dbname=database, user=user, password=password, host=host, port = port)

cur = con.cursor()

# create input data table
#cur.execute("CREATE TABLE input_data (ID SERIAL PRIMARY KEY, input_label TEXT);")

#create predictions table
#cur.execute("CREATE TABLE predictions (ID SERIAL PRIMARY KEY, prediction TEXT);")

#train the model and store it
#also make it available in this script
#import main
#model = main.model

#store test data, test label, prediction label

#cur.execute("CREATE TABLE input_data (ID SERIAL PRIMARY KEY, input_label varchar);")
cur.execute("CREATE TABLE predictions (ID SERIAL PRIMARY KEY, prediction varchar);")


cur.execute('''
CREATE SEQUENCE idsequence
    start 10
    increment 1;''')



#execute query
#cur.execute("select * from input_data;")
#print ("These are the inputs that have been tested so far:")
#print(cur.fetchall())


#cur.execute("select * from predictions;")
#print ("The CNN predicted the tested inputs to be:")
#print(cur.fetchall())


#commit data to db
con.commit()
con.close()


#store test data, test label, prediction label

def savingtestresult(pred_label):
#def savingtestresult(test_label, test_data, pred_label):

    host = "postgres"
    database = "milestone5"
    port = "5432"
    user = "postgres"
    password = "pgpass"

    con = psycopg2.connect(dbname=database, user=user, password=password, host=host, port = port)
    cur = con.cursor()

    #savingtestresult.counter += 1
    #load testdata into database input_data
    cur.execute("insert into predictions (ID, prediction) values (nextval('idsequence'), %s)", (pred_label,))

    #execute query
    #cur.execute("select * from input_data;")
    #image1 = np.fromstring(cur.fetchall()[-1], dtype = int).reshape(32,32,3)
    #print ("These are the inputs that have been tested so far:")
    #print(cur.fetchall()[-1], image1)

    #cur.execute("select * from predictions;")
    #print ("The CNN predicted the tested inputs to be:")
    #print(cur.fetchall())
    #commit data to db
    con.commit()
    con.close()
#savingtestresult.counter = 0

def printdatabase():
    host = "postgres"
    database = "milestone5"
    port = "5432"
    user = "postgres"
    password = "pgpass"

    con = psycopg2.connect(dbname=database, user=user, password=password, host=host, port = port)

    cur = con.cursor()
    #my_table = pd.read_sql_table('table_name', connection)
    my_table = pd.read_sql('select * from predictions', con)
    #another_attempt= psql.read_sql("SELECT * FROM input_data", con)

    return my_table

    # OR
    #print(another_attempt) 
    con.close()


