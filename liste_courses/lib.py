import logging

LOGGER = logging.getLogger()


class Liste(list):
    def __init__(self, nom):
        self.nom = nom

    def ajouter(self, element):
        if not isinstance(element, str):
            raise ValueError("Vous ne pouvez ajouter que de chaînes de caractères")
        if element in self:
            LOGGER.error(f"{element} est déjà dans la liste")
        self.append(element)
        return True
    
    def enlever(self, element):
        if element in self:
            self.remove(element)
            return True
        return False



if __name__ == "__main__":
    print("Hello")