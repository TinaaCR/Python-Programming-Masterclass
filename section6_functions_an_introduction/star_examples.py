numbers = (0, 1, 2, 3, 4, 5)

# print(numbers, sep=";")

# print(*numbers, sep=";") # er det samme som å skrive print(1, 2, 3, 4, 5). vi pakker ut tuble ved å skrive stjerne
# print(0, 1, 2, 3, 4, 5, sep=";")


def test_star(*args):
    print(args)
    for x in args:
        print(x)

test_star(1, 2, 3, 4, 5)

print()
test_star()