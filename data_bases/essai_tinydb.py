from tinydb import TinyDB, Query, where
db = TinyDB('data.json', indent = 4)

db.insert({"name": "Patrick", "score":0})
db.insert_multiple([
    {"name": "Marc", "score":0},
    {"name": "Julie", "score":5},
    {"name": "Fred", "score":10}
])

User = Query()
patrick = db.search(User.name =="Patrick")
print(patrick)

high_scores = db.search(where("score")> 1)
print(high_scores)
print(db.count(User.name =="Patrick"))
print(db.contains(User.name =="Patrick"))
print(db.contains(User.name =="patrick")) 
print(len(db))

db.update({"score": 12}, where("name")=="Patrick")
print(patrick)

db.update({"roles": ["Junior"]})
db.update({"roles": ["Pythonista"]}, where("name") =="Patrick")
db.upsert(
    {"name": "Eric", "score": 20, "roles": ["Senior"]}, 
    where("name") == "Eric"  
) #ajoute à la fin ou modifie si existe déjà