list1 = eval(input("Geef lijst met minimaal 10 strings: "))

list(list1)
index = 1
for values in list1:
	if index < len(list1):
		
		print("De nieuw-gemaakte lijst met alle vier-letter strings is:"+list1[index][2])
	index += index