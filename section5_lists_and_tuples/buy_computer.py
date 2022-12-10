available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "hdmi",
                   "dvd drive"
                   ]
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]  # kommer tilbake til denne måten å kode på senere

valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))    # ved å skrive str (står for string) konverterer vi til string formatet

print(valid_choices)

current_choice = "-"    # trenger en startverdi. betyr ikke så mye hva det er så lenge det ikke er i konflikt med noen av verdiene vi har tenkt å gi den senere
computer_parts = []     # create empty list

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # it's already in so remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains {}".format(computer_parts))
    else:
        print("Please select item from the list below:")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()

print(computer_parts)       # når indentation er helt til venste så utføres denne delen av koden helt til slutt i programmet