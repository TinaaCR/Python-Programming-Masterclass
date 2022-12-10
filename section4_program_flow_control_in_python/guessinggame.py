import random


def get_integer(prompt):
    """
    Get an input from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.
    :param prompt: The string that the user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{} is not a valid number".format(temp))


# print(input.__doc__)
# print("*" * 80)
# print(get_integer.__doc__)
# print("*" * 80)

help(get_integer)

highest = 1000
answer = random.randint(1, highest)
print(answer) # TODO: remove after testing
guess = 0   # initialise to any number that does not equal the answer

print("Please select a number between 1 - {}: ".format(highest))

while guess != answer:

    guess = get_integer(": ")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry you guessed incorrectly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry you guessed incorrectly")
# else:
#     print("You got it first time")

# Her kommer en enklere måte å skrive samme kode på som i eksempelet over (det som ligger som kommentarer #):

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else: # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry you guessed incorreclty")
# else:
#     print("You got it first time")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else: # guess must be greater than answer
            print("Please guess lower")
        #     guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        # else:
        #     print("Sorry you guessed incorreclty")