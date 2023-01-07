import random

def terning(antall_sider, antall_ganger):
    prosent = 1
    for i in range(1, antall_ganger+1):
        terning = random.randint(1, int(antall_sider))
        print("terning: " + str(terning))

        prosent = (i / antall_sider) * prosent


    return prosent




print(terning(6, 5))


#husk å print mange ganger forskjellige steder i koden for å se hva som skjer
#husk å bruk en variabel som du først lar være feks 1 og så endres ved å legge til seg selv. se linje 4 og 9.