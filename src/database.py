import mysql.connector

def open_db():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3307,
        user='root',
        password='root',
        database='gestion_nettoyage_classes',
        buffered=True,
        autocommit=True
    )