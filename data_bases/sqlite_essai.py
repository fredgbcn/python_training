import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()
c.execute("""
 CREATE TABLE IF NOT EXISTS employees(
          prenom text,
          nom text
          )         
          
""")
d = {"a": "Paul", "b": "Dupond"}
e = {"a" : "Marc", "b": "Sérault"}
c.execute("INSERT INTO employees (prenom, nom) VALUES (:a, :b)", d)
c.execute("INSERT INTO employees (prenom, nom) VALUES (:a, :b)", d)
c.execute("DELETE FROM employees WHERE prenom=:a AND nom=:b", d)

c.execute("SELECT * FROM employees")
donnees = c.fetchall()
print(donnees)
conn.commit()

conn.close()