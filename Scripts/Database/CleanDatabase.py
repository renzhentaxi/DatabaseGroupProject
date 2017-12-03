#removes all tables in the database
import psycopg2

conn = psycopg2.connect("dbname=mydb user=tashit")
cur = conn.cursor()

cur.execute("DROP TABLE employees")
cur.execute("DROP TABLE salesleads")
cur.execute("DROP TABLE accounts")

conn.commit()
cur.close()
conn.close()