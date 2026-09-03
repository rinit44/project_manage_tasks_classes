# name : import_data_class.py
# author : Rinit Krasniqi
# date : 03.09.2026
from database import insert_classes

def import_data_classes():
    classes_to_insert = []

    with open("data/raw/classes.csv", encoding="cp1252") as file:
        next(file)
        for line in file:
            line_clean = line.strip()
            if line_clean:
                name, room = line_clean.split(";")
                classes_to_insert.append((name, room))

    if classes_to_insert:
        insert_classes(classes_to_insert)

    print("Importation terminée.")

if __name__ == "__main__":
    import_data_classes()