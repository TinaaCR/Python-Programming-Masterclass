# kan bruke formattering for å få tallene på linje ved å sette inn [:tall] som vist i eksempelet under. feks det første tallet er maks
# to siffer, mens de andre tallene er maks 3 og 4:
for i in range(1, 13):
    print("No.  {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

# for å få tallene venstrestilte kan man bruke < tegnet:
for i in range(1, 13):
    print("No.  {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print()

# kan også sentralisere tallene ved å bruke ^ tegnet:
for i in range(1, 13):
    print("No.  {0:2} squared is {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))     # f står for floating point value (foat er tall med desimal(er)). gir default 6 desimaler etter komma
print("Pi is approximately {0:12.50f}".format(22 / 7))  # i dette tilfellet, siden 50 desimaler er større enn det området vi har spesifisert (12 desimaler) velger python allikvel å printe 50 desimaler siden python vurderer presisjonen som viktigere enn vidden på feltet
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7)) # her har vi venstrestilt
print("Pi is approximately {0:<72.54f}".format(22 / 7)) # her har vi venstrestilt og i tillegg lagt til 4 desimaler

print()

# man kan fortsatt bruke denne formelen unden å spesifisere hvor man henter fra, men isåfall vil første gang man henter være fra posisjon 0 osv:
for i in range(1, 13):
    print("No.  {} squared is {} and cubed is {}".format(i, i ** 2, i ** 3))

print()

# og man kan fremdeles legge til vidden [:tall] uten å spesifisere hvor man henter fra:
for i in range(1, 13):
    print("No.  {:2} squared is {:3} and cubed is {:4}".format(i, i ** 2, i ** 3))
