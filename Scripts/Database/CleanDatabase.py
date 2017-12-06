import psycopg2

print("Cleaning database")
conn = psycopg2.connect("dbname=renzhentaxibaerde user=renzhentaxibaerde")
cur = conn.cursor()


cur.execute("DROP Table IF EXISTS salesleads;")
cur.execute("DROP Table IF EXISTS employees;")
cur.execute("DROP Table IF EXISTS accounts;")
cur.execute("DROP TYPE IF EXISTS jobrole;")

conn.commit()
cur.close()
conn.close()
print("done")
