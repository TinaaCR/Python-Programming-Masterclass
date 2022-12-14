import shelve

books = shelve.open("book")

books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "beans on toast": ["beans", "bread"],
                    "scrambled eggs": ["eggs", "butter", "milk"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "cheese"]}
books["maintenence"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}

print(books["recipes"])
# print(books["recipes"]["scrambled eggs"])
#
# print(books["maintenence"]["loose"])

books.close()

