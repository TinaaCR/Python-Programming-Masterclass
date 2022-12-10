empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)   # numbers og sorted_numbers er lister så å sortere disse gir også lister

# digits = sorted("432985617")    # hvis vi ikke ønsker å sortere tallene i stringen, kunne vi skrevet list istedenfor storted. dette vil alltid gi en liste
digits = list("432985617")
print(digits)   # output her vil gi en liste med strings, siden digits er en string

# more_numbers = list(numbers)
# more_numbers = numbers[:]   # dette er også en måte å lage en liste
more_numbers = numbers.copy()
print(more_numbers)
print(numbers is more_numbers)  # inneholder samme tall i samme rekkefølge, men er ikke samme liste, så svaret vil bli False
print(numbers == more_numbers)  # inneholder samme tall i samme rekkefølge og er dermed like så denne blir True