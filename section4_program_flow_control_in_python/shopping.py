shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

# koden over kan skrives på en annen måte med "continue":

# for item in shopping_list:
#     if item == "spam":
#         continue
#
#     print("Buy " + item)

# det som skjer her er at for loopen går som vanlig helt frem til den kommer til "spam" da vil den utføre koden på rad 10
# og deretter 11 og det continue gjør er at den hopper automatisk tilbake til rad 9 istedenfor ned til 13.

# en annen funksjon som kan brukes er "break":

for item in shopping_list:
    if item == "spam":
        break

    print("Buy " + item)