# nå skal vi se på nested for loops. dvs at vi har en for loop inni en annen for loop

for i in range(1, 13):
    for j in range(1, 13):
        print("{0} times {1} is {2}".format(j, i, i * j))
print("------------")