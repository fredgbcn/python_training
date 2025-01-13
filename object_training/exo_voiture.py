class Voiture:
    essence = 100
    distance_totale = 0
    def __init__(self, distance_totale):
        self.distance_totale = distance_totale    

    def roule(self, km):
        essence_necessaire = (km * 5)/100
        print(f"il faut {essence_necessaire} L pour faire {km} km")
        if essence_necessaire > self.essence :
            print("Vous n'avez plus assez d'essence, faites le plein")
        else :
            self.distance_totale += km
            print(f"vous avez parcouru {self.distance_totale} en tout")
            
            self.essence = self.essence - essence_necessaire
            if self.essence <= 10 :
                print("Vous n'avez bientôt plus d'essence")
    
    def afficher_reservoir(self):
        print(f"Il reste {self.essence} L d'essence")

    def faire_le_plein(self):
        self.essence = 100
        print("Et c'est reparti !")

v = Voiture(0)
