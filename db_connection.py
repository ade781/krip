# db_connection.py

import mysql.connector


def connect_db():
    return mysql.connector.connect(
        host="sql12.freesqldatabase.com",
        user="sql12745170",
        password="eYApSiTED4",
        database="sql12745170",
        port=3306
    )
