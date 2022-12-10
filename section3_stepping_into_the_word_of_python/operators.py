a = 12
b = 3

print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0 (division gir alltid foat resultat, dvs tall med desimal. for å forhindre dette kan vi bruke // som vist under).
print(a // b)   # 4 integer (int) division, rounded down to minus infinity
print(a % b)    # 0 modulo: the remainder after integer division

print()

print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print((((a + b)/3) - 4) * 12)
print(((a + b) / 3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print()

print(a / (b * a) / b)



