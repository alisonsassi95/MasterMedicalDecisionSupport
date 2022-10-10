import csv
import psycopg2
conn = psycopg2.connect(database="dadijunvuu9gm3",
                        user='doxtibbjpjckmm', password='41ec522c36b1e43c28b1e830f4c82ceb4ff124707fae212f63b07654a85631d0', 
                        host='ec2-44-207-133-100.compute-1.amazonaws.com', port='5432'
)
cursor = conn.cursor()
print("Passou aqui 0.")
with open('NameFileExport.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    print("Passou aqui 1.")
    for row in reader:
        print("Passou aqui 2.")
        cursor.execute('''INSERT INTO patient (name_patient,neurological,MeaningNeurological,cardiovascular,MeaningCardiovascular,respiratory,MeaningRespiratory,coagulation,MeaningCoagulation,hepatic,MeaningHepatic,renal,MeaningRenal,spict,MeaningSpict,ecog,MeaningEcog,scoreSOFA,scoreAmib,group_patient,classification,active,exported,validatedDoctor,justification) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)''', row)
        print("Passou aqui 3.")
conn.commit()





conn.autocommit = True
cursor = conn.cursor()
  
  
sql = '''SELECT * FROM patient;'''

cursor.execute(sql) 

for i in cursor.fetchall():
    print("entrou!")
    print(i)

  
sql2 = '''COPY patient(name_patient,neurological,MeaningNeurological,cardiovascular,MeaningCardiovascular,respiratory,MeaningRespiratory,coagulation,MeaningCoagulation,hepatic,MeaningHepatic,renal,MeaningRenal,spict,MeaningSpict,ecog,MeaningEcog,scoreSOFA,scoreAmib,group_patient,classification,active,exported,validatedDoctor,justification) FROM 'NameFileExport.csv' DELIMITER ',';'''
  
cursor.execute(sql2)
  
sql3 = '''select * from details;'''
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)
  
conn.commit()
conn.close()