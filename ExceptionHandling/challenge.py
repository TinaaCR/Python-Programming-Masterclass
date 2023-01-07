
tall1 = input("velg et tall: ")
tall2 = input("velg et tall: ")

#svar = 0

def multiplisering():
    svar = int(tall1) / int(tall2)
    print(svar)

try:
    print(multiplisering())
except ValueError:
    print("Obs, du må velge et tall")



# fasit:
import sys

def getint(prompt):
    while True: # denne gjør at loopen fortsetter helt til man oppgir et gyldig tall
        try:
            number = int(input(prompt))
            return number # denne gjør at man kommer seg ut av loopen med en gang et gyldig tall blir gitt
        except ValueError:
            pint("invalid number entered, please try another")
        except EOFError:
            sys.exit(1)
        finally:
            print("The finally clause always executes")


first_number = getint("velg et første tall ")
second_numer = getint("velg et andre tall ")

try:
    print("{} divided by {} is {}".format(first_number, second_numer, first_number / second_numer))
except ZeroDivisionError:
    print("cant divide numbers by zero")
    sys.exit(2)
else:
    print("Division performed successfully")



