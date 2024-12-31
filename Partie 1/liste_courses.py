import json

sauvegarde = r'C:\Users\fgauf\Desktop\Code\python\udemy\Partie 1\ma_liste.json'

def charger_liste(fichier):
    """Charge la liste depuis le fichier JSON."""
    try:
        with open(fichier, "r", encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return [] 
        
def sauvegarder_liste(fichier, liste):
    """Sauvegarde la liste dans le fichier JSON."""
    with open(fichier, "w", encoding='utf-8') as f:
        json.dump(liste, f, indent=4)

def menu():
    """Affiche le menu et retourne le choix de l'utilisateur."""
    print("\nMenu :")
    print("1: Ajouter un élément à la liste")
    print("2: Retirer un élément de la liste")
    print("3: Afficher la liste")
    print("4: Vider la liste")
    print("5: Quitter")
    return input("👉 Votre choix : ")

def main():
    # Charger la liste au démarrage
    liste = charger_liste(sauvegarde)
    print(f"Votre liste contient ceci au démarrage : {liste}")
    
    while True:
        choix = menu()
        if choix == "1":
            element = input("Entrez un élément à ajouter : ")
            liste.append(element)
            print(f"'{element}' a été ajouté à la liste.")
            sauvegarder_liste(sauvegarde, liste)  # Sauvegarder après modification
        elif choix == "2":
            element = input("Entrez l'élément à retirer : ")
            if element in liste:
                liste.remove(element)
                print(f"'{element}' a été retiré de la liste.")
                sauvegarder_liste(sauvegarde, liste)  # Sauvegarder après modification
            else:
                print(f"'{element}' n'est pas dans la liste.")
        elif choix == "3":
            if liste:
                print("Voici la liste :")
                for i, item in enumerate(liste, 1):
                    print(f"{i}. {item}")
            else:
                print("La liste est vide.")
        elif choix == "4":
            liste.clear()
            print("La liste a été vidée.")
            sauvegarder_liste(sauvegarde, liste)  # Sauvegarder après modification
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez choisir une option entre 1 et 5.")

if __name__ == "__main__":
    main()
