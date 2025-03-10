import mysql.connector


def connect_db():
    return mysql.connector.connect(
        host="35.225.207.4",
        user="root",
        password="",
        database="kripto",
        port=3306
    )
