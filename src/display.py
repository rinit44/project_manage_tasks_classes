def show_menu():
    print("\n" + "=" * 45)
    print("     GESTION DE L'ORDRE EN CLASSE")
    print("=" * 45)
    print("1. Afficher l’ordre en classe")
    print("2. Générer le planning « Ordre en classe »")
    print("3. Valider l’ordre en classe de la semaine")
    print("4. Supprimer un élève de la liste")
    print("5. Ajouter un élève de la liste")
    print("6. Générer le document « Ordre en classe »")
    print("7. Sortir du menu")
    print("=" * 45)

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
            print("Supprimer un eleve")
        elif choix == "5":
            print("ajouter un eleve")
        elif choix == "6":
            print("generer le doc")
        elif choix == "7":
            print("\nAu revoir !")
            break
        else:
            print("Option invalide. Choisis un nombre entre 1 et 7.")

if __name__ == "__main__":
    choice()