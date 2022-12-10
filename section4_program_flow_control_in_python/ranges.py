# på samme måte som string slices returerer karakterer opp til men IKKE inkludert det siste
# tallet gjør for loops også dette. den siste spesifiserte verdien blir IKKE inkludert
# range produserer verdier fra startverdien, og opp til men IKKE inkludert sluttverdien

for i in range(10, 0, -2):
    print("i is now {}".format(i))
