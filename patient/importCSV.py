import csv
import psycopg2

conn = psycopg2.connect(database="d8dqiu239l9c22",
                        user='bsnsqyayiqdchl', password='b1fc0d3119362454988c120f43bc974166c1935de605354596183b33266d9382', 
                        host='ec2-44-194-92-192.compute-1.amazonaws.com', port='5432'
)
cursor = conn.cursor()
with open('../NameFileExport.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        tran = str(row)[1:-1]
        #insert_query = "INSERT INTO patient (name_patient,neurological,MeaningNeurological,cardiovascular,MeaningCardiovascular,respiratory,MeaningRespiratory,coagulation,MeaningCoagulation,hepatic,MeaningHepatic,renal,MeaningRenal,spict,MeaningSpict,ecog,MeaningEcog,scoreSOFA,scoreAmib,group_patient,classification,active,exported,validatedDoctor,justification) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)", tran
        insert_records = "INSERT INTO patient (name_patient,neurological,\"MeaningNeurological\",cardiovascular,\"MeaningCardiovascular\", respiratory,	\"MeaningRespiratory\",	coagulation,\"MeaningCoagulation\",	hepatic,\"MeaningHepatic\",	renal,\"MeaningRenal\",	spict,\"MeaningSpict\",	ecog,\"MeaningEcog\",\"scoreSOFA\",\"scoreAmib\",group_patient,	classification,	active,	exported,\"validatedDoctor\", justification) VALUES(" + tran + ",0,'TRUE','TRUE',0,'NULL')"
        cursor.execute(insert_records)

conn.commit()
cursor.close()
conn.close()