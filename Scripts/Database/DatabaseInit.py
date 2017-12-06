import psycopg2

tableDefinition = {}


tableDefinition["employees"] = """
    CREATE TABLE IF NOT EXISTS employees (
    employeeId INT UNIQUE PRIMARY KEY,
    firstName VARCHAR(80),
    lastName VARCHAR(80),
    userName VARCHAR(80) UNIQUE REFERENCES accounts (userName),
    position jobrole
    );
"""


tableDefinition["accounts"] = """
    CREATE TABLE IF NOT EXISTS accounts (
    accountId int UNIQUE PRIMARY KEY,
    userName varchar(80) UNIQUE,
    password varchar(80)
    );
"""


tableDefinition["salesleads"] = """
    CREATE TABLE IF NOT EXISTS salesleads (
    leadsId int UNIQUE PRIMARY KEY,
    firstName varchar(80),
    lastName varchar(80),
    companyName varchar(255),
    address varchar(255),
    city varchar(255),
    county varchar(255),
    state varchar(255),
    zip int,
    phone1 varchar(20),
    phone2 varchar(20),
    email varchar(255),
    web varchar(255),
    salesRepId int REFERENCES employees (employeeid)
    )
"""

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

