import mysql.connector
from database import open_db

def import_students():
    db_connection = open_db()
    cursor = db_connection.cursor()

    query_insert = """
        INSERT INTO students (firstname, lastname, mail, class_id)
        SELECT %s, %s, %s, id 
        FROM classes 
        WHERE classe_name = %s
    """

    with open("data/raw/students.csv", encoding="utf-8") as file:
        next(file)
        for line in file:
            firstname, lastname, mail, room = line.strip().split(";")
            
            cursor.execute(query_insert, (firstname, lastname, mail, room))

    cursor.close()
    db_connection.close()
    print("Importation terminée.")


    import_students()