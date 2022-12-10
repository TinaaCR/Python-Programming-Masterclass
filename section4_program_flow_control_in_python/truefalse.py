# bruk av boolean values; True, False, or, and, not

# day = "Saturday"
# temperature = 30
# raining = True
# # kan være lurt å bruke parantes (selv om ikke python krever det), pga det gjør det tydeligere hva som hører sammen. "and" har høyere "verdi" enn "not":
# if (day == "Saturday" and temperature > 27) or not raining:
#     print("Go swimming")
# else:
#     print("Learn Python")

if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name ")
# if name:
if name != "":  # bedre å skrive det på denne måten i starten
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")