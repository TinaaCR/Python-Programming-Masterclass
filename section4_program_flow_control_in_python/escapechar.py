# \n splitter en string til ny linje som vist i eksempel under:
split_string = "This string has been\nsplit over\nseveral\nlines"
print(split_string)

# \t gir ekstra mellomrom mellom verdier i en string som vist i eksempelet under:
tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string)

# hvis man skal bruke både "" og '' i en string kan man sette \ i mellom verdien som vist i eksemplene under.
# alternativet er å bruke 3x hastag:
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")
print("""The pet shop owner said "No, no, \
'e's uh,...he's resting". """)

# hvis man bruke 3x hastag kan man starte på en ny linje og output vil bli på ny linje. legger man \ på slutten av
# linjen vil denne effekten kanselleres og all teksten vil komme på samme linje
another_split_string = """This string has been \
split over \
several \
lines"""

print(another_split_string)

# hvis du står på en linje og trykker ctrl + d så kopieres det som står i denne linjen til neste linje

# print("C:\Users\timbuchalka\notes.txt")
# hvis man ønsker at linjen over faktisk skal printe \ så kan dette gjøres på to måter (men det er anbefalt å bruke \\):
print("C:\\Users\\timbuchalka\\notes.txt")
print(r"C:\Users\timbuchalka\notes.txt")

# refactoring code betyr å endre på strukturen til koden, men uten å endre hvordan koden oppfører seg/ hva den gjør
# man kan endre på feks et variabelnavn ved å høyreklikke på navnet, trykke på refactor og så rename og endre navnet på variabelen. da vil navnet for den variabelen oppdateres alle steder hvor det blir brukt