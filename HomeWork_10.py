# Expand previous Homework 5/6/7/8/9 with additional class, which allow to save records into database:
# 1.Different types of records require different data tables
# 2.New record creates new row in data table
# 3.Implement “no duplicate” check.

import pyodbc
# import sqlite3
# import datetime
# import os
# import HomeWork_5_1 as Post


class DBConnetion:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self, database_name):
        self.conn = pyodbc.connect(f'Driver=SQLite3 ODBC Driver;Database={database_name};Direct=True;String Types=Unicode' )
        self.cur = self.conn.cursor()

    def select(self, field, table):
        self.cur.execute(f'select {field} from {table}')
        return self.cur.fetchall()

    def insert(self, table, field1, field2, field3):
        self.cur.execute(f"""INSERT INTO {table} VALUES ({field1},{field2},{field3})""")
        self.cur.commit()

    def create_table(self, table, field1, field2, field3):
        self.cur.execute(f"CREATE TABLE {table} ({field1} varchar(255), {field2} varchar(255), {field3} varchar(255))")
        self.cur.commit()

    def close_conn(self):
        self.conn.close()



# connection = pyodbc.connect('Driver=SQLite3 ODBC Driver;Database=test.db;Direct=True;String Types=Unicode')
# cursor = connection.cursor()


# cursor.execute('CREATE TABLE people (first_name text, last_name text, age real)')
# cursor.execute("INSERT INTO people VALUES ('Ivanov' , 'Ivan' ,'32')")
# connection.commit()
# cursor.execute("select * from people")
# result = cursor.fetchall()
# print(result)
# cursor.close()
# connection.close()

dbconn= DBConnetion()

dbconn.connect('test2.db')
# dbconn.create_table('New', 'first_name', 'city', 'data')
# dbconn.create_table('Ad', 'text', 'data_until', 'days')
# dbconn.create_table('Recipe', 'text', 'complexity', 'data')
dbconn.insert('New', 'text', 'city', 'data')
a = dbconn.select('*', 'New')
print(a)
dbconn.close_conn()