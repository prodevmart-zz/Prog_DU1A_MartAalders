def seizoen(maandnummer): 
	
	 
	if maandnummer == 12 or 1 or 2:
		return print("Winter")
	elif maandnummer == 3 or 4 or 5:
		return print("Lente")
	elif maandnummer == 6 or 7 or 8:
		return print("Zomer")
		
	elif maandnummer == 9 or 10 or 11:
		return print("Herfst")
		

print(seizoen(12))