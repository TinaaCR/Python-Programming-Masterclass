import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 12345, 'tim@mail.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 56789, 'brian@mail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())


for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-"*20)


cursor.close()
db.commit() # OBS! her sier vi at vi faktisk skal gjøre selve oppdateringen. uten commit skjer det ingen endring i databasen.
db.close()