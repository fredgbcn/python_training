from tinydb import TinyDB, Query, where
db = TinyDB('data.json', indent = 4)

db.insert({"name": "Patrick", "score":0})
db.insert_multiple([
    {"name": "Marc", "score":0},
    {"name": "Julie", "score":5},
    {"name": "Fred", "score":10}
])