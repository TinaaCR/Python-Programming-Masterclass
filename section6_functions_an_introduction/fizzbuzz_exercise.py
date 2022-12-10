# function that returns the next answer
# game played with 2 or more people
# you start counting, in turn. but if the number is divisible by 3 you say "fizz" instead
# if it is divisible with 5 you say "buzz" instead
# if it is divisible by both 3 and 5 you say "fizz buzz"

# your function should return the correct word, fizz, buzz, fizz buzz or the number if it is not divisible by 3, 5 or 3 and 5
# the function will always return a string. when you return the number you should convert it to a string first


def fizz_buzz(number: int) -> str:
    """
    the function shall return the correct word, fizz, buzz or fizz buzz if it is divisible by 3, 5 and 3 and 5 respectively.
    If not the function shall return the number as a string
    :param number: choose number to enter game
    :return: return string based on input
    """
    if number % 3 == 0 and number % 5 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)



# for i in range(1, 101):
#     print(fizz_buzz(i))


# exercise 2.0:
# the computer will execute with the value 1 and then the player will type in a response. then they will take turns.
# the game ends when the player makes a mistake or gets to 100
# if the player gets it wrong they lose


input("Play Fizz Buzz.    Press ENTER to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    # players_answer = correct_answer
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("Well done, you reached {}".format(next_number))





