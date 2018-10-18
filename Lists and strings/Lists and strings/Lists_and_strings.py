ListWith10Strings = eval(input("Geef lijst met minimaal 10 strings: "))
NewList = []
for string in ListWith10Strings:
	if len(string) == 4:
		NewList.append(string)
print(NewList)