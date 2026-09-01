import mysql.connector
from database import open_db


def import_classes():
    db_connection = open_db()
    cursor = db_connection.cursor()

    query_insert = """
        INSERT INTO classes (name, room)
        VALUES (%s, %s)
    """

    with open("data/raw/classes.csv", encoding="utf-8") as file:
        next(file)
        for line in file:
            name, room = line.strip().split(";")
            cursor.execute(query_insert, (name, room))

    cursor.close()
    db_connection.close()
    print("Importation terminée.")

if __name__ == "__main__":
    import_classes()