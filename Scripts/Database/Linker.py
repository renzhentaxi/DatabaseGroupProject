import psycopg2
import sys
from sshtunnel import SSHTunnelForwarder

try:
    with SSHTunnelForwarder(
            'compsci.adelphi.edu',
            ssh_username="renzhentaxibaerde",
            ssh_password="hpCmQ2GI",
            remote_bind_address=('localhost', 5432)
    ) as server:
        server.start()
        print("server connected")
        params = {
            'database': 'renzhentaxibaerde',
            'user': 'renzhentaxibaerde',
            'password': 'password',
            'host': 'localhost',
            'port': 5432
        }

        conn = psycopg2.connect(**params)
        curs = conn.cursor()

        print("database connected")
except:
    print("connection failed")
    print(sys.exc_info())
