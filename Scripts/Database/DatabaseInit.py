import psycopg2
import sys,os

sys.path[0] = os.getcwd()
from Scripts.Database.TableDefinition import tableDefinition

print("Initializing database")
conn = psycopg2.connect("dbname=renzhentaxibaerde user=renzhentaxibaerde")
cur = conn.cursor()

cur.execute("CREATE TYPE jobRole AS ENUM ('rep', 'man');")
cur.execute(tableDefinition["accounts"])
cur.execute(tableDefinition["employees"])
cur.execute(tableDefinition["salesleads"])

conn.commit()
cur.close()
conn.close()
print("done")
