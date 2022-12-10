# ved bruk av string funksjonen (str) kan man konvertere fra int (tall) til string (tekst):
age = 24
print("my age is " + str(age) + " years")

# en mer effektiv metode som er mulig i python 3:
print("my age is {0} years".format(age))

#  man kan sette inn flere verdier ved å bruke denne metoden som vist under:
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Aug: {1}, Sep: {2}, Oct: {1}, Nov: {2}, Dec: {1}"
      .format(28, 30, 31))

print()

print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Aug: {1}
Sep: {2}
Oct: {1}
Nov: {2}
Dec: {1}""".format(28, 30, 31))
