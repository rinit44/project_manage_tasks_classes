# name : database.py
# author : Rinit Krasniqi
# date : 03.09.2026
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


def insert_classes(classes_data):
    db_connection = open_db()
    cursor = db_connection.cursor()

    query_insert = """
        INSERT IGNORE INTO classes (classe_name, classroom)
        VALUES (%s, %s)
    """

    for student in classes_data:
        cursor.execute(query_insert, student)

    cursor.close()
    db_connection.close()


def insert_students(students_data):
    db_connection = open_db()
    cursor = db_connection.cursor()

    query_insert = """
        INSERT IGNORE INTO students (firstname, lastname, mail, class_id)
        SELECT %s, %s, %s, id 
        FROM classes 
        WHERE classe_name = %s
    """

    for student in students_data:
        cursor.execute(query_insert, student)

    cursor.close()
    db_connection.close()