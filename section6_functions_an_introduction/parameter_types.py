def func(p1, p2, *args, k, **kwargs): # p1, p2 posisjons parametre, *args (aksepterer et variabel av argumenter), k er et nøkkelord parameter, kwarg står for nøkkelord argumenter
    print("positional-or-keyword:...{}, {}".format(p1, p2))
    print("var-positional (*args):..{}".format(args))
    print("keyword..................{}".format(k))
    print("var-keyword..............{}".format(kwargs))


func(1, 2, 3, 4, 5, k=6, key1=7, key2=8)


def sum_numbers(p1, p2, p3):
    """
    get numbers and return sum
    :param p1: input parameter 1
    :param p2: input parameter 2
    :param p3: input parameter 3
    :return: sum of parameters
    """
    svar = p1 + p2 + p3
    return svar


print("{}, {}, {} results in {}".format(2.1, 3.1, 4.5, sum_numbers(2.1, 3.1, 4.5))
