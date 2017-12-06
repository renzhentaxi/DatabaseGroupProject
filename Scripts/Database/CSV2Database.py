import psycopg2

def load_from_csv(cur, csv_path, table_name):
    print("Creating the", table_name, "table")
    f = open(csv_path +table_name + ".csv")
    cur.copy_from(f,table_name)



params = {
    'database' : 'mydb',
    'user' :'renzhentaxibaerde',
    'password' : '',
    'host' : 'renzhentaxibaerde@compsci.adelphi.edu'

}
conn = psycopg2.connect("dbname=renzhentaxibaerde user=renzhentaxibaerde")
cur = conn.cursor()

load_from_csv(cur, "./data/csv/", "accounts")
load_from_csv(cur, "./data/csv/", "employees")
load_from_csv(cur, "./data/csv/", "salesleads")

conn.commit()
cur.close()
conn.close()
print("done")