

def factorial(x: int):
    """
    function that returns the factoral of x
    :param x: input x value
    :return: factoral of x
    """
    svar = 1
    for i in range(1, x + 1):
        svar *= i
    return svar




for x in range(0, 36):
    print("{0}" " " "{1}".format(x, factorial(x)))


# svar = svar * i
# svar = 1 * 1
# svar = 1 * 2
# svar = 2 * 3
# svar = 6 * 4
# svar = 24 * 5