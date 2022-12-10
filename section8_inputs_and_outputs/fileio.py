# jabber = open("/Users/Tina/Desktop/sample.txt", 'r')    # r-en står for read. pga vi ønsker å lese filen
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# jabber.close() # husk å alltid lukke filen når du er ferdig hvis ikke kan den bli korrupt (?)
#
# with open("/Users/Tina/Desktop/sample.txt", 'r') as jabber: # siden vi har en with setning er det ikke nødvendig å lukke sample.txt filen etterpå (???)
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("/Users/Tina/Desktop/sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='') # end='' gjør at vi ikke printer ekstra linjer
#         line = jabber.readline()


# with open("/Users/Tina/Desktop/sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')

with open("/Users/Tina/Desktop/sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')

with open("/Users/Tina/Desktop/sample.txt", 'r') as jabber:
    lines = jabber.read()
print(lines)

for line in lines[::-1]:
    print(line, end='')

