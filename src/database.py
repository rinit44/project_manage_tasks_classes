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
        INSERT IGNORE INTO classes (class_name, classroom)
        VALUES (%s, %s)
    """

    for classe in classes_data:
        cursor.execute(query_insert, classe)

    cursor.close()
    db_connection.close()


def insert_students(students_data):
    db_connection = open_db()
    cursor = db_connection.cursor()

    query_insert = """
        INSERT IGNORE INTO students (firstname, lastname, mail, class_id)
        SELECT %s, %s, %s, id 
        FROM classes 
        WHERE class_name = %s
    """

    for student in students_data:
        cursor.execute(query_insert, student)

    cursor.close()
    db_connection.close()

def search_student(firstname, lastname, class_name):
    db_connection = open_db()
    cursor = db_connection.cursor()

    query_search = """
        SELECT students.id, students.firstname, students.lastname, classes.class_name
        FROM students
        JOIN classes ON students.class_id = classes.id
        WHERE students.firstname = %s 
        AND students.lastname = %s 
        AND classes.class_name = %s
    """
    cursor.execute(query_search, (firstname, lastname, class_name))
    result = cursor.fetchone()

    cursor.close()
    db_connection.close()

    return result


def delete_student(student_id):
    db_connection = open_db()
    cursor = db_connection.cursor()

    try:
        cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        success = True
    except mysql.connector.IntegrityError:
        success = False
    finally:
        cursor.close()
        db_connection.close()

    return success


def insert_student(firstname, lastname, mail, class_name):
    if not mail.endswith("@eduvaud.ch"):
        raise ValueError("ce email ne fait pas partie du domaine eduvaud")

    if not any(char.isalpha() for char in mail):
        raise ValueError("l'email doit contenir au moins une lettre")
        

    db_connection = open_db()
    cursor = db_connection.cursor()

    cursor.execute("""
        INSERT INTO students (firstname, lastname, mail, class_id)
        SELECT %s, %s, %s, id
        FROM classes
        WHERE class_name = %s
    """, (firstname, lastname, mail, class_name))
    success = cursor.rowcount > 0

    cursor.close()
    db_connection.close()

    return success