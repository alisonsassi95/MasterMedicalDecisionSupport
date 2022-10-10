import psycopg2
import csv

conn = psycopg2.connect(database="dadijunvuu9gm3",
                        user='doxtibbjpjckmm', password='41ec522c36b1e43c28b1e830f4c82ceb4ff124707fae212f63b07654a85631d0', 
                        host='ec2-44-207-133-100.compute-1.amazonaws.com', port='5432'
)
  
conn.autocommit = True
cursor = conn.cursor()
  
sql2 = '''COPY details(employee_id,employee_name,\
employee_email,employee_salary)
FROM '/private/tmp/details.csv'
DELIMITER ','
CSV HEADER;'''
  
cursor.execute(sql2)
  
sql3 = '''select * from details;'''
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)
  
conn.commit()
conn.close()