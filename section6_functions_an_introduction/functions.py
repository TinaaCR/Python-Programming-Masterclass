def multiply(x: float, y: float) -> float:  # float er tall med desimal
    """
    Get a value x multiplied with a value y
    :param x: input value x
    :param y: input value y
    :return: x multiplied by y
    """
    result = x * y
    return result

# OBS: det må kommer to tomme linjer (som her) etter en funskjon
def is_palindrome(string: str) -> bool: # str er forkortelse for "string"
    """
    Get a string and check if it is a palindrome or not.
    A palindrome is a string that reads the same forwards and back
    :param string: the string to check
    :return: the string is returned if it is a palindrome (True) else it is not returned (False)
    """
    # backwards = string[::-1]    # denne slicen reverserer den originale stringen
    # return backwards == string  # hvis backwards er lik string så blir denne True og returned. hvis de ikke er like blir det falske og ikke returned
    return string[::-1].casefold() == string.casefold()


# word = input("Please enter a word to check: ")
#
# if is_palindrome(word):
#     print("{} is a palindorme".format(word))
# else:
#     print("{} is not a palindrome".format(word))

def palindrome_sentence(sentence: str) -> bool:
    string = ""
    for char in sentence:
        if char.isalnum():  # hvis denne er True, dvs hvis vi har bokstav eller tall (dvs ikke et tegn)
            string += char  # så legges tallet eller bokstaven til
    #    return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)



# answer = multiply(10.5, 4)  # gir float resultat pga 10.5 er en float
# print(answer)
#
# forty_two = multiply(6, 7)  # gir int resultat siden både 6 og 7 er int
# print(forty_two)
#
# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)

answer = multiply(18, 3)
print(answer)


def fibonacci(n: int) -> int:   # int står for "integer" og er et tall
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1,0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))


p = palindrome_sentence()