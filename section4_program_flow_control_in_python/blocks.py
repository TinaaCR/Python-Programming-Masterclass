# når man lager et kolon, dvs : på slutten av en kodelinje forventer python at det skal være en ny kode-blokk

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {}".format(i, i ** 2, i ** 3))
    print("*" * 80)

# bruk av input funksjonen:
# name = input("Please enter your name: ")
# age = input("How old are you, {0}?".format(name))
# print(age)

# kan også skrives med int som vist under, men dette krever at du skriver et tall. hvis ikke får du feilmelding:
name = input("Please enter your name: ")
age = int(input("How old are you, {0}?".format(name)))
print(age)

# bruk av is og else funksjon:
#if age >= 18:
#   print("you are old enough to vote")
#   print("Please put an X in the box")
#else:
#   print("Please come back in {0} years".format(18 - age))

# kan også snu på det:
# if age < 18:
#   print("Please come back in {0} years".format(18 - age))
# else:
#   print("you are old enough to vote")
#   print("Please put an X in the box")

# bruk av else-if funksjonen, elif:
if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry Yoda, you die in the return of the jedi")
else:
    print("you are old enough to vote")
    print("Please put an X in the box")

# TIPS: for å gjøre om kode til kommentar (dvs skrive # forran) så hold inne Ctrl + Fn + 0


