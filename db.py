import os
import sqlite3
from typing import Text, List


class DataBase:
    def __init__(self):
        super(DataBase, self).__init__()
        self.db_name: Text = "garage_db.db3"
        self.db_exist: bool = os.path.exists(self.db_name)
        self.conn = sqlite3.connect(f'./{self.db_name}')
        self.cursor = self.conn.cursor()
        if self.db_exist is False:

            # employee
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS employees(ID INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
                    SURNAME	TEXT NOT NULL COLLATE BINARY,
                    FIRST_NAME TEXT NOT NULL COLLATE BINARY,
                    PATRONYMIC TEXT NOT NULL COLLATE BINARY,
                    EMPLOYMENT_DATE TEXT NOT NULL COLLATE BINARY,
                    UNIQUE('SURNAME','FIRST_NAME','PATRONYMIC'))
                    """)

            self.cursor.execute("""CREATE TABLE IF NOT EXISTS orders(ID INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
                   EMPLOYEE_ID INTEGER NOT NULL,
                   VEHICLE_ID TEXT NOT NULL COLLATE BINARY,
                   REPAIR_COST TEXT NOT NULL COLLATE BINARY,
                   BREAKDOWN_DESCRIPTION TEXT NOT NULL COLLATE BINARY,
                   REPAIR_DATE_START TEXT NOT NULL COLLATE BINARY,
                   REPAIR_DATE_END TEXT NOT NULL COLLATE BINARY,
                   FOREIGN KEY("EMPLOYEE_ID") REFERENCES employees(ID),
                   FOREIGN KEY("VEHICLE_ID") REFERENCES vehicle(ID))
                   """)
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS vehicle(ID INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
                    VEHICLE_BRAND	TEXT NOT NULL COLLATE BINARY,
                    VEHICLE_MODEL TEXT NOT NULL COLLATE BINARY,
                    REG_NUMBER TEXT NOT NULL COLLATE BINARY,
                    UNIQUE('VEHICLE_BRAND','VEHICLE_MODEL','REG_NUMBER'))""")

            self.cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS id_employee ON employees (ID COLLATE BINARY DESC)")
            self.cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS id_order ON orders (ID COLLATE BINARY DESC)")
        else:
            pass

    def insert(self, query):
        self.cursor.execute(query)
        self.conn.commit()
        return self.cursor.lastrowid

    def update(self, query):
        self.cursor.execute(query)
        self.conn.commit()
        return self.cursor.lastrowid
    # UPDATE "main"."orders" SET "BREAKDOWN_DESCRIPTION"=? WHERE "_rowid_"='1004'

    def getting(self, field: List, table: Text, method: Text, custom_body: Text = ""):
        field_query: Text = ""
        query: Text = ""
        for i in field:
            if field_query is "":
                field_query += str(i)
            else:
                field_query += "," + str(i)
        if method == "simple":
            query: Text = "SELECT {0} FROM {1}".format(field_query, table)
        elif method == "custom":
            query: Text = "SELECT {0} FROM {1} {2}".format(field_query, table, custom_body)

        return self.cursor.execute(query).fetchall()

    def __del__(self):
        self.conn.close()

