
# to terninger hvor summen skal bli 8
# antall treff

variabel = 0

for i in range(1, 7):
    #print(i)
    for y in range(1, 7):
        print("terning 1: " + str(i)  + " terning 2: " + str(y))

        if y + i == 8:
            print("sum: ", i + y)
            variabel = variabel + 1
cmdprint(variabel)

