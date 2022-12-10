
# setning_tuple = ("Hei på deg din ku du er et svin i en sølepytt")
# setning = setning_tuple.lower()
# setning = set(setning_tuple)
#
#
# setning.discard("a")
# setning.discard("e")
# setning.discard("i")
# setning.discard("o")
# setning.discard("u")
#
# print(sorted(setning))

# sånn det egentlig skulle gjøres:

sampleText = "Python is a powerful language"

vowels = frozenset("aeiou")
finalSet = set(sampleText).difference(vowels)
print(sorted(finalSet))
