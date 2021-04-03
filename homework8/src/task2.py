"""
Task
====
Write a wrapper class TableData for database table, that when initialized with database name and table acts as collection object (implements Collection protocol).
Assume all data has unique values in 'name' column.
So, if presidents = TableData(database_name='example.sqlite', table_name='presidents')

then
 -  `len(presidents)` will give current amount of rows in presidents table in database
 -  `presidents['Yeltsin']` should return single data row for president with name Yeltsin
 -  `'Yeltsin' in presidents` should return if president with same name exists in table
 -  object implements iteration protocol. i.e. you could use it in for loops::
       for president in presidents:
           print(president['name'])
 - all above mentioned calls should reflect most recent data. If data in table changed after you created collection instance, your calls should return updated data.

Avoid reading entire table into memory. When iterating through records, start reading the first record, then go to the next one, until records are exhausted.
When writing tests, it's not always necessary to mock database calls completely. Use supplied example.sqlite file as database fixture file.
"""
import os
import sqlite3


class TableData:
    def __init__(self, database_name, table_name):
        file_path = os.path.join(os.path.dirname(__file__), database_name)
        if os.path.isfile(file_path):
            self.database_name = file_path
        else:
            raise FileNotFoundError

        self.conn = self.init_connection(table_name)
        self.table_name = table_name
        self.cursor = self.conn.cursor()

    def init_connection(self, table_name):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"
        )
        if cursor.fetchone() is None:
            raise sqlite3.DatabaseError("No such table")
        conn.row_factory = sqlite3.Row
        return conn

    def __del__(self):
        if hasattr(self, "conn"):
            self.conn.close()

    def __len__(self):
        self.cursor.execute(f"SELECT count(*) from {self.table_name}")
        return self.cursor.fetchone()[0]

    def __getitem__(self, key):
        self.cursor.execute(f"SELECT * from {self.table_name} WHERE name='{key}'")
        item = self.cursor.fetchone()
        if item:
            return dict(item)

    def __contains__(self, key):
        return self[key] is not None

    def __iter__(self):
        self.cursor.execute(f"SELECT * from {self.table_name}")
        return self

    def __next__(self):
        row = self.cursor.fetchone()
        if not row:
            raise StopIteration
        return dict(row)
