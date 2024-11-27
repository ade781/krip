import mysql.connector


def connect_db():
    return mysql.connector.connect(
        host="6xdib.h.filess.io",
        user="kripto_beingever",
        password="a3badf670f3e69c9fe35d6e9688eeeccc6d0b8b5",
        database="kripto_beingever",
        port=3307
    )
