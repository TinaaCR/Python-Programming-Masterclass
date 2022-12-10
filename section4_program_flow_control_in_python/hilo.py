low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
while low != high:  # dette betyr at loopen vil fortsette for evig. må skrive det sånn siden vi ikke vet hva svaret er
    # print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should i guess higher or lower? "
                     "Enter h or l, or c if my guess was correct "
                     .format(guess)).casefold()   # ved å trykke code + reformat code i menyen over så får man en lang kode på riktig rekke
    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        # pass # pass gjør ikke noe, men gjør at syntaksen (?) blir korrekt. kan ikke skrive "...kode:" og så ikke skrive noe mer under. "pass" kan brukes som en placeholder for koden du vil legge til senere
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes 1 less than the guess.
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break

    else:
        print("Please enter h, l or c")

    # guesses = guesses + 1. dette gir samme output som koden under. men koden under er bedre pga guesses blir bare evaluert en gang istedenfor hver gang:
    guesses += 1

else:
    print("You though of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))