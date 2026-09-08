# name : import_data_students.py
# author : Rinit Krasniqi
# date : 03.09.2026
from database import insert_students

def import_data_students():
    students_to_insert = []

    with open("data/raw/students.csv", mode="r", encoding="cp1252") as file:
        next(file)
        for line in file:
            line_clean = line.strip()
            if line_clean:
                firstname, lastname, mail, room = line_clean.split(";")
                students_to_insert.append((firstname, lastname, mail, room))

    if students_to_insert:
        insert_students(students_to_insert)

    print("Importation terminée.")

if __name__ == "__main__":
    import_data_students()