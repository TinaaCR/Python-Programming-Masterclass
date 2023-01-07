import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "newemail@update.com"
phone = input("Please enter phone number ")

# update_sql = "UPDATE contacts SET email = '{}' WHERE contacts.phone = {}".format(new_email, phone)
update_sql = "UPDATE contacts SET email = ? WHERE contacts.phone = ?"
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))
print("{} rows updated".format(update_cursor.rowcount))

print()
print("Are connections the same: {}".format(update_cursor.connection == db))
print()

update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-"*20)


update_cursor.connection.commit() # viktig å koble spesifikk cursor til commit funksjonen. da du ikke vil bli varselt om commit ikke fungerer og denne typen feil er vanskelig å spotte i ettertid.

db.close()
