import mysql.connector


def connect_db():
    return mysql.connector.connect(
        host="sql205.infinityfree.com	
",
        user="if0_37801178",
        password="DVMQw2JvhNFWi",
        database="if0_37801178_kripto",
        port=3306
    )
