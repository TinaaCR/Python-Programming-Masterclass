letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]
print(backwards)

# forrige eksempel printer alt uten bokstaven a, men hva må vi gjøre for å få med a også? jo vi gjør som vist under:
backwards = letters[25::-1]
print(backwards)

# eller:
backwards = letters[::-1]   # vanlig å skrive det sånn i python og det kalles reversing the sequence. kalles python ideom
print(backwards)

# challenge
første = letters[16:13:-1]  # skal printe ut qpo
print(første)

andre = letters[4::-1]  # skal printe ut edcba
print(andre)

tredje = letters[25:17:-1]  # skal printe ut zyxwvuts
print(tredje)

print(letters[-4:])
print(letters[-1:])

print(letters[:1])
# eller
print(letters[0])
