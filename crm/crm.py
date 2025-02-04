import re
import string
from tinydb import TinyDB, where
from pathlib import Path

class User:

    DB = TinyDB(Path(__file__).resolve().parent / "db.json", indent = 4)
    def __init__(self, first_name: str, last_name: str, phone_number: str="", address: str=""):
        self.first_name = first_name
        self.last_name = last_name 
        self.phone_number = phone_number
        self.address = address
        self.a = 5
    def __repr__(self) -> str:
         return f"User({self.first_name}, {self.last_name})"
    def __str__(self):
            return f"User({self.first_name} {self.last_name}, {self.phone_number}, {self.address})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}" 
    
    @property
    def db_instance(self):
        return User.DB.get((where('first_name') == self.first_name) & (where('last_name') == self.last_name))

    def _check_phone_number(self):
         phone_number = re.sub(r"[+()\s]*", "", self.phone_number)
         if len(phone_number) < 10 or not phone_number.isdigit():
            raise ValueError(f"Numéro de téléphone {self.phone_number} invalide.")
    def _check_names(self):
         if not (self.first_name and self.last_name):
            raise ValueError("Le prénom et le nom de famille ne peuvent pas êtres vides")   
         special_characters = string.punctuation + string.digits
         for character in self.first_name + self.last_name :
             if character in special_characters:
                 raise ValueError(f"Nom invalide {self.first_name}.")
    def _checks(self):
        self._check_phone_number()
        self._check_names()

    def exists(self):
        return bool(self.db_instance)

    def delete(self):
        instance = self.db_instance
        if instance and isinstance(instance, dict) and "doc_id" in instance:
            User.DB.remove(doc_ids=[instance.doc_id])

    def save(self, validate_data: bool=False) -> int:
        if validate_data:
            self._checks()
        return User.DB.insert(self.__dict__)  
    
def get_all_users():
    valid_keys = {"first_name", "last_name", "phone_number", "address"}
    return [User(**{k: user[k] for k in valid_keys if k in user}) for user in User.DB.all()]


if __name__ == "__main__":
    from faker import Faker
    fake = Faker("fr_FR")
    for _ in range(10):
        user = User(first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    phone_number=fake.phone_number(),
                    address=fake.address())
        user._checks()
        print(user)
        user.save()
        print(user.full_name)
        print(repr(user))
        print("-" *10)
        simone = User("Simone", "Morel")
        print(simone.delete())
