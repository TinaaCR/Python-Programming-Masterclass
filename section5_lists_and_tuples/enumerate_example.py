# for index, character in enumerate("abcdefgh"):
#     print

for t in enumerate("abcdefgh"):
    index, character = t    # et eksempel på unpacking tuples
    print(index, character)


index, character = (0, 'a')
print(index)
print(character)
