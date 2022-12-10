computer_parts = ["computer",
                  "keyboard",
                  "monitor",
                  "mouse",
                  "mouse mat"
                  ]

# for part in computer_parts:
#     print(part)
#
# print()
# print(computer_parts[2])    # husk at indeks nummereringen starter på 0, og derfor blir indeks 2 monitor i dette tilfelle
#
# print(computer_parts[0:3])  # slicing a list creates another list, dvs vi får [] som output også
# print(computer_parts[-1])   # printer ut siste item i listen

print(computer_parts)

# computer_parts[3] = "trackball" # samme som å si s[i] = x. vi erstatter i med x.
print(computer_parts[3:])

computer_parts[3:] = ["trackball"]
print(computer_parts)
