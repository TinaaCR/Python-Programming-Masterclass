# et pangram inneholder alle bokstaver i alfabetet minst en gang

pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)   # sorted funksjonen tar hvilken som helst iterable men returnerer en liste
print(letters)  # å printe letters gir nå en sortert versjon av pangram. tegn først så store bokstaver og så små bokstaver.

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)    # sorted funksjonen fungerer også for tall
print(sorted_numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumps over the lazy dog",
                        key=str.casefold)   # viktig at man her fjerner parantesene i casefold() pga vi skal ikke kalle funksjonen i dette tilfelle.
                                            # key=str.casefold gir case insensitive sorting, som betyr at man sorterer uten å ta hensyn til om det er stor eller liten bokstav
print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
        ]

names.sort(key=str.casefold)
print(names)
