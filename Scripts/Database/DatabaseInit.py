import psycopg2

conn = psycopg2.connect("dbname=mydb user=tashit")
cur = conn.cursor()

cur.execute( "CREATE TYPE jobRole AS ENUM ('rep', 'man');")

conn.commit()
cur.close()
conn.close()
print("done")
