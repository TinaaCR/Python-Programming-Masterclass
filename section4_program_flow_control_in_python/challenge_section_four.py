# skrive et program som viser forskjellige valgmuligheter, og lar brukeren velge noe fra listen
# valgene skal numereres fra 1 til 9 (eller minst 4)
# programmet skal fortsette i loop for å tillate brukeren å gjøre et valg for hver gang
# programmet skal kun stanse når brukeren velger "0"
# hvis brukeren gjør et gyldig valg skal programmet printe ut en liten beskjed og inneholde verdien de la inn

one = "1. Svømme"
two = "2. Sykle"
three = "3. Løpe"
four = "4. Ski"
five = "5. Fjelltur"
six = "6. Ingen av delene, avslutt ved å skrive 0"

list = ["1. Svømme", "2. Sykle", "3. Løpe", "3. Løpe", "4. Ski", "5. Fjelltur", "6. Ingen av delene, avslutt ved å skrive 0"]

print("velg mellom disse aktivitetene: \n"+one+"\n"+two+"\n"+three+"\n"+four+"\n"+five+"\n"+six+"\n")

chosen_exit = ""
while chosen_exit not in list:
    chosen_exit = input("Velg hvilken aktivitet du vil gjøre: ")
    if chosen_exit == "0":
        print("avslutter")
        break
    else:
        print("dette valget finnes ikke")
else:
    print("Du valgte {}".format(chosen_exit))


# løsningen var:

print("Please choose your option from the list:")
print("1:\tLearn Python")
print("2:\tLearn Java")
print("3:\tGo Swimming")
print("4:\tHave dinner")
print("1:\tGo to bed")
print("0:\tExit")

while True:
    choice = input()
    if choice == 0:
        break
    elif choice in "12345":
        print("Your choice was {}".format(choice))


# kan også skrives uten å bruke "break" og hvor man også får menyen på nytt hvis man velger noe som ikke finnes i menyen:

choice = "-"    # her kunne man i teorien gitt choice hva som helst av verdi, utenom 1-5 eller 0 siden disse allerede er "tatt". men vi er nødt til å definere choice før vi bruker den i koden:
while choice != "0":
    if choice in "12345":
        print("Your choice was {}".format(choice))
    else:
        print("Please choose your option from the list:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo Swimming")
        print("4:\tHave dinner")
        print("1:\tGo to bed")
        print("0:\tExit")

    choice = input()
