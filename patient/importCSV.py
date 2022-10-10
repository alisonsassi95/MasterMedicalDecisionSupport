import csv
import psycopg2
conn = psycopg2.connect(database="dadijunvuu9gm3",
                        user='doxtibbjpjckmm', password='41ec522c36b1e43c28b1e830f4c82ceb4ff124707fae212f63b07654a85631d0', 
                        host='ec2-44-207-133-100.compute-1.amazonaws.com', port='5432'
)


cursor = conn.cursor()

cursor.execute('SELECT * FROM patient')
all = cursor.fetchall()
print("---all->")
print(all)
with open('NameFileExport.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        print("list->")
        print(list(row))
        res = str(row)[1:-1]
        print("res->")
        print(res)
        insert_query = ("INSERT INTO patient (name_patient,neurological,MeaningNeurological,cardiovascular,MeaningCardiovascular,respiratory,MeaningRespiratory,coagulation,MeaningCoagulation,hepatic,MeaningHepatic,renal,MeaningRenal,spict,MeaningSpict,ecog,MeaningEcog,scoreSOFA,scoreAmib,group_patient,classification,active,exported,validatedDoctor,justification) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)", row)
        print("------------")
        print(insert_query)
        cursor.execute(list(insert_query))
        print("Passou aqui 3.")
conn.commit()
cursor.close()
conn.close()