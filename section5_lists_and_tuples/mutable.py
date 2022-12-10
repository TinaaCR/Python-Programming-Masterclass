shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice",
                 ]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))    # her vil id fortsatt være den samme siden vi kan endre shopping_list til å inkludere flere items uten å endre id
print(another_list) # denne har samme verdi som shopping_list pga vi har allerede sagt at disse er lik hverandre

a = b = c = d = e = f = another_list
# koden på linjen over er det samme som å skrive:
# a = another_list
# b = another_list
# c = another_list
# d = another_list
# e = another_list
# f = another_list
print(a)

print("Adding cream")
b.append("cream")
print(c)
print(d)

print(shopping_list)
print(another_list)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)