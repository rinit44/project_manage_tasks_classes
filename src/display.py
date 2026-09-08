# name : display.py
# author : Rinit Krasniqi
# date : 03.09.2026
from src import database

def show_menu():
    print("\n" + "=" * 45)
    print("     GESTION DE L'ORDRE EN CLASSE")
    print("=" * 45)
    print("1. Afficher l'ordre en classe")
    print("2. Générer le planning « Ordre en classe »")
    print("3. Valider l'ordre en classe de la semaine")
    print("4. Supprimer un élève de la liste")
    print("5. Ajouter un élève de la liste")
    print("6. Générer le document « Ordre en classe »")
    print("7. Sortir du menu")
    print("=" * 45)

def ask_and_search_student():
    firstname = input("Prénom de l'élève : ").strip()
    lastname = input("Nom de l'élève : ").strip()
    classe_name = input("Classe de l'élève : ").strip()

    eleve = database.search_student(firstname, lastname, classe_name)

    if eleve is None:
        show_student_not_founded()
        return None

    return eleve

def show_finded_student(firstname, lastname, classe):
    print(f"\nÉlève trouvé : {firstname} {lastname} - Classe : {classe}")

def show_student_not_founded():
    print("Aucun élève trouvé avec ces informations.")

def show_deletion_student():
    print("L'élève a bien été supprimé.")

def show_deletion_cancelled():
    print("Suppression annulée.")


def handle_student_deletion():
    student = ask_and_search_student()
    if student is None:
        return

    student_id, fn, ln, classe = student
    show_finded_student(fn, ln, classe)

    confirmation = input("Confirmez-vous la suppression de cet élève ? (o/n) : ").strip().lower()

    if confirmation == "o":
        success = database.delete_student(student_id)
        if success:
            show_deletion_student()
        else:
            print("Impossible de supprimer cet élève : il est encore lié à un planning de nettoyage.")
    else:
        show_deletion_cancelled()


def ask_student_info():
    firstname = input("Prénom de l'élève : ").strip()
    lastname = input("Nom de l'élève : ").strip()
    mail = input("Email de l'élève : ").strip()
    classe_name = input("Classe de l'élève : ").strip()

    return firstname, lastname, mail, classe_name


def show_insertion_success():
    print("L'élève a bien été ajouté.")

def show_insertion_failed():
    print("Impossible d'ajouter l'élève (classe introuvable ou email déjà utilisé).")


def handle_student_insertion():
    firstname, lastname, mail, classe_name = ask_student_info()

    success = database.insert_student(firstname, lastname, mail, classe_name)

    if success:
        show_insertion_success()
    else:
        show_insertion_failed()



def choice():
    while True:
        show_menu()
        choix = input("Choisis une option (1-7) : ").strip()

        if choix == "1":
            print("l'ordre en classe")
        elif choix == "2":
            print("Générer le planning")
        elif choix == "3":
            print("Valider l'ordre en classe de la semaine")
        elif choix == "4":
            handle_student_deletion()
        elif choix == "5":
            handle_student_insertion()
        elif choix == "6":
            print("generer le doc")
        elif choix == "7":
            print("\nAu revoir !")
            break
        else:
            print("Option invalide. Choisis un nombre entre 1 et 7.")