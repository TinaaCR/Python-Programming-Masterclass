
with open("/Users/Tina/Desktop/sample.txt", 'a') as regning:
    for x in range(1,11):
        for number in range(1,13):
            regning.write("{} times {} is {} \n".format(number, x, number*x))
        regning.write("-"*20)
