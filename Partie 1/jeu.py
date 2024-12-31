
import random
import sys

random_number_attack = random.randint(5, 10)
random_number_ennemi_attack = random.randint(5, 15)
random_number_potion = random.randint(15, 50)
ma_vie = 50
vie_ennemi = 50
nombre_potions = 3


while True:
    print("Souhaitez-vous attaquer ? Tapez 1, Prendre une potion ? Tapez 2")
    choix = input()   
    try:
        # Tente de convertir l'entrée en entier
        nombre = int(choix)
        # Vérifie si l'entier est 1 ou 2
        if nombre in [1, 2]:
            if nombre == 1 :
                vie_ennemi = vie_ennemi-random_number_attack 
                ma_vie = ma_vie - random_number_ennemi_attack
                print(f"Vous avez infligé {random_number_attack} points de dégât à l'ennemi, il lui reste {vie_ennemi} points de vie")
                print(f"L'ennemi vous a infligé {random_number_ennemi_attack} de dégats, il vous reste {ma_vie} points de vie")
            elif nombre == 2:
                if nombre_potions > 0:
                    ma_vie = random_number_potion + ma_vie
                    nombre_potions -= 1
                    print(f"Vous avez utilisé une potion ! Vous avez gagné {random_number_potion} points de vie. Vous avez {ma_vie} points de vie, il vous reste {nombre_potions} potions.")
                    ma_vie = ma_vie - random_number_ennemi_attack
                    print(f"L'ennemi vous a infligé {random_number_ennemi_attack} de dégats, il vous reste {ma_vie} points de vie et il reste {vie_ennemi} à l'ennemi")
                else:
                    print("Vous n'avez plus de potions !")
            #Vérification nombre de points de vie
            if ma_vie <= 0:
                print("Vous avez perdu, votre vie est à 0 !")
                break  # Le jeu s'arrête ici si le joueur meurt

            if vie_ennemi <= 0:
                print("Vous avez gagné ! L'ennemi est à 0 points de vie.")
                break  # Le jeu s'arrête ici si l'ennemi meurt

        else:
            print("L'entrée est un entier, mais la valeur doit être 1 ou 2.")
            print("Souhaitez-vous attaquer ? Tapez 1, Prendre une potion ? Tapez 2")
            choix = input()
    except ValueError:
        # Si une erreur survient, ce n'est pas un entier
        print("L'entrée n'est pas un entier.")
        print("Souhaitez-vous attaquer ? Tapez 1, Prendre une potion ? Tapez 2")
        choix = input()


    