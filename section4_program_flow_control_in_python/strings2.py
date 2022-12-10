# #  hvordan bruke indeks []. ordet Norwegian Blue har følgende indeksering/ indeks posisjoner (startet på 0):
# #         012345678901234
# parrot = "Norwegian Blue"
#
#
# print(parrot)
#
# print(parrot[3])
# print(parrot[13])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])
#
# print()
#
# # man kan gjøre indeksing i motsatt rekkefølge også ved å bruke minus. ordet Norwegian Blue har da indeksering fra - 1 til - 14.
# print(parrot[-11])
# print(parrot[-10])
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])
#
# print()
# # istedenfor negativ indeksering kan man også skrive på denne måten:
# print(parrot[3 - 14])
# print(parrot[13 - 14])
# print(parrot[9 - 14])
# print(parrot[3 - 14])
# print(parrot[6 - 14])
# print(parrot[8 - 14])
#
# print()

# print(parrot[0:6]) # print norweg. printer fra indeks 0 til 6, men uten å ta med nr 6. UP TO BUT NOT INCLUDING!
# print(parrot[3:5])
# print(parrot[0:9])
# print(parrot[:9])
# print(parrot[10:])
# print(parrot[10:14])
#
# print(parrot[:6])
# print(parrot[6:])
# print(parrot[:6] + parrot[6:])
#
# print(parrot[:])

# nå skal vi se på negative slices:

#         012345678901234
# parrot = "Norwegian Blue"

# print(parrot[-4:-2])    # Bl
# print(parrot[-4:12])    # Bl

# print(parrot[0:6])
# print(parrot[-14:-8])
# print(parrot[3:5])
# print(parrot[-11:-9])
# print(parrot[0:9])
# print(parrot[-14:-6])
# print(parrot[:9])
# print(parrot[-6:])
# print(parrot[10:])
# print(parrot[-4:])
# print(parrot[10:14])

# print(parrot[:6])
# print(parrot[6:])
# print(parrot[:6] + parrot[6:])
# print(parrot[:-5])
# print(parrot[-5:])
# print(parrot[:-5] + parrot[-5:])

# nå skal vi bruke steg i en slice:
# her fungerer de to første posisjonene som normalt (dvs som i eksemplene over), mens den tredje sier noen om hvor mange steg vi skal ta

# print(parrot[0:6:2])    # Nre
# print(parrot[0:6:3])    # Nw

# et eksempel på bruk som er for avansert for det nivået vi er på nå:

# number = "9,223;372:036 854,775;807"
number = input("Please enter a series of numbers, using any separators you like: ")
# separators = number[1::4]
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char
# print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum(([int(val) for val in values])))

