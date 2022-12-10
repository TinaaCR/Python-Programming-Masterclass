# activity = input("What would you like to do today? ")
#
# if "cinema" not in activity.casefold(): # ved å bruke .casefold så spiller det ikke noe rolle om input inneholder små eller store bokstaver
#     print("But I want to go to the cinema")

name = input("What is your name? ")
age = int(input("What is you age? ")) # viktig å huske å konvertere input til int i dette tilfelle

if age >= 18 and age < 31:
    print("Welcome to the holiday, {}".format(name))
else:
    print("Sorry you are not the appropriate age")
