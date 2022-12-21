import sqlite3

conn = sqlite3.connect("contacts.sqlite")

name = input("hvem vil du ha ")


for rows in conn.execute("SELECT * FROM contacts WHERE name = ?", (name,)): # kan bruke LIKE istedenfor =. da bryr den seg ikke om små/ store bokstaver
    print(rows)

conn.close()
