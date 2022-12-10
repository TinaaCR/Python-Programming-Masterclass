print("Today is a good day to learn Python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " word")
greeting = "Hello"
# name = input("Please enter your name ")
name = "Tim"
print(greeting + name)

# if we want a space we can add that too
print(greeting + ' ' + name)

age = 24
print(age)

print(type(greeting))
print(type(age))

# man gi en variabel (feks age) en ny verdi, feks en string istedenfor en int som i eksempelet under:
age = "2 years"
print(age)
print(type(age))

# for å hindre forvirring kan det være lurt å lage en ny variabel istedenfor:
age_in_words = "2 years"

# man kan ikke kombinere (concatenate) en string og en int, feks print(name + "is" + age + "years old") vil
# gi feilmelding pga age = 24 og et tall kan ikke legges til en string

# kan også bruke noe som heter en f string. dette kan gjøres ved å legge til en f som vist i eksempelet under:
age = 24
print(name + f" is {age} years old")
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")

