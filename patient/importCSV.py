# Import required modules
import csv
import sqlite3
import os
import psycopg2

# Connecting to the geeks database
#connection = sqlite3.connect('db.sqlite3')
conn = psycopg2.connect(database="dadijunvuu9gm3",
                        user='doxtibbjpjckmm', password='41ec522c36b1e43c28b1e830f4c82ceb4ff124707fae212f63b07654a85631d0', 
                        host='ec2-44-207-133-100.compute-1.amazonaws.com', port='5432'
)
conn.autocommit = True
cursor = conn.cursor()

print("Deu certo a Conexão")
  
# Creating a cursor object to execute
# SQL queries on a database table
cursor = conn.cursor()

# Table Definition
#create_table = '''CREATE TABLE person(
#               id INTEGER PRIMARY KEY AUTOINCREMENT,
#                name TEXT NOT NULL,
#                age INTEGER NOT NULL);
#                '''
  
# Creating the table into our 
# database
#cursor.execute(create_table)
  
# Opening the .csv file
file = open('NameFileExport.csv', newline='', encoding='utf-8')
  
# Reading the contents of the 
# person-records.csv file
contents = csv.reader(file)

#deveria tirar a primeira linha
  
# SQL query to insert data into the
# person table
insert_records = "INSERT INTO patient (name_patient,neurological,MeaningNeurological,cardiovascular,MeaningCardiovascular,respiratory,MeaningRespiratory,coagulation,MeaningCoagulation,hepatic,MeaningHepatic,renal,MeaningRenal,spict,MeaningSpict,ecog,MeaningEcog,scoreSOFA,scoreAmib,group_patient,classification,active,exported,validatedDoctor,justification) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,0,1,0,0,'')"
  
# Importing the contents of the file 
# into our person table
cursor.executemany(insert_records, contents)
  
# SQL query to retrieve all data from
# the person table To verify that the
# data of the csv file has been successfully 
# inserted into the table
select_all = "SELECT * FROM patient"
rows = cursor.execute(select_all).fetchall()
  
# Output to the console screen
for r in rows:
    print(r)
  
# Commiting the changes
conn.commit()
  
# closing the database connection
conn.close()