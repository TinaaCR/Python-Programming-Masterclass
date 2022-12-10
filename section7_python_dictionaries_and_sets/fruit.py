fruit = {"orange": "a sweet, orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favorite",
       "sprouts": "mmmm, lovely",
       "spinach": "can I have som more fruit, please"}

print(veg)

veg.update(fruit)
print(veg)

print(fruit.update(veg))

nice_and_nasty = fruit.copy() # best å bruke copy pga da endrer man ikke den originale dictionary som heter fruit i dette tilfelle, man bare kopierer den
nice_and_nasty.update(veg)
print(nice_and_nasty)
