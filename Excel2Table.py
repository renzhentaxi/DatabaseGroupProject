from openpyxl import *
import sqlite3


def convertSalesReps(workbook):
    db = sqlite3.connect("database\database")
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE salesReps(id INTEGER PRIMARY KEY, fname TEXT, lname TEXT, userName TEXT)
''')
    db.commit()
    db.close()
    
convertSalesReps(load_workbook("excels\SalesReps.xlsx"))
