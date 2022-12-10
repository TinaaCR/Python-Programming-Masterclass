available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break

else:
    print("aren't you glad you got out of there")

# en viktig fordel med while loop er at den kan brukes i tilfeller hvor det ikke kan bestemmes på forhånd hvor mange ganger
# programmet må kjøre gjennom en loop