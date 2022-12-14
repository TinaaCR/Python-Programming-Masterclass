fruit = {"orange": "a sweet, orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)
# print(fruit["lemon"])   # lemon i dette tilfelle er en "key" som når vi printer printer informasjonen om denne, som en ordbok
#
# # kan legge til i ordboken:
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# # hvis vi gir key-ordet en ny verdi blir den gamle verdien erstattet av den nye:
# fruit["pear"] = "great with tequila"
# print(fruit)
# # kan slette key-ord
# del fruit["lemon"]
# print(fruit)
# # det er også mulig å tømme listen:
# fruit.clear()
# print(fruit)

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     # description = fruit.get(dict_key, "We don't have a " + dict_key)
#     # print(description)
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("we don't have a " + dict_key)


# for snack in fruit:
#     print(fruit[snack])

# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print("-" * 40)
#

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])

# keys i fruit-dictionary er apple, grape, lemon, lime og orange. vi skal også printe kun verdiene ved å bruke .values():

for val in fruit.values():
    print(val)


print(fruit.keys())
print(fruit.values())


# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)

print(fruit)
print(fruit.items())

f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)


print(dict(f_tuple))