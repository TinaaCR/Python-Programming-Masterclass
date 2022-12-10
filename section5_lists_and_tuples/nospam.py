menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]


# challenge:
# printe ut alle måltidene med uten stringen "spam"
# kan enten velge å fjerne spam fra hver liste og så printe den, eller
# printe hvert item i listen utenom spam
# bør skrive to koder med begge tilnærmingene

for meal in menu:
    for index in range(len(meal) - 1, - 1, - 1):    # tror det er denne delen av koden som gjør at vi går gjennom hele listen i hvert "meal"
        if meal[index] == "spam":   # meal[index]. her refererer indeks til posisjonen til item i listen
            del meal[index]
    print(", ".join(meal))


# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item, end= " ") # denne koden printer ut menyene uten at de er i en liste, bare hvert item
#     print()



