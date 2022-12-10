# hvis du har en tuple vil output være i parantes istedenfor klammer. det viser at du har en tuple og ikke en liste
# det er egentlig ikke nødvendig i bruke parantes rundt a,b,c under, men i enkelte tilfeller med tuples er det nødvendig, derfor kan det være greit å alltid bruke det:
# t = ("a", "b", "c")
# print(t)

welcome = "Welcome to my Nighmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the lightning", "Metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# # største forskjellen mellom tuples og lists er at tuples er immutable, dvs de kan ikke endres. en stor fordel med tuples er at de krever mye mindre minne og man kan unngå å klundre til data underveis i koden ved å gi den ny verdi ved et uhell feks
#
# # kan gjøre tuples om til lister:
# metallica2 = list(metallica)
# print(metallica2)
#
# # lister kan endres, som vist under:
# metallica2[0] = "Master of Puppets"
# print(metallica2)

title, artist, year = metallica
print(title)
print(artist)
print(year)

table = ("Coffee table", 200, 100, 75, 34.50)
print(table[1] * table[2])

# istedenfor print-koden over kan vi heller unpack tuples og dermed gjøre den lettere å lese:

name, length, width, height, price = table
print(length * width)

albums = [("Welcome to my Nighmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the lightning", "Metallica", 1984)
          ]

print(len(albums))

for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))

