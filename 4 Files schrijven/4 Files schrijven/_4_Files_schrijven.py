import os
import datetime 
vandaag = datetime.datetime.today() 
s = vandaag.strftime("%a %d %b %Y"+", "+"%H"+":"+"%S"+":"+"%M"+",") 


i = 0
while i >= 0:
	exists = os.path.isfile('hardlopers.txt')
	naam = input("Wat is de naam van de hardloper?")
	print(s,naam)
	if exists:
			file = open("hardlopers.txt","a")
			file.write(s+ naam+ "\n")
	else:
		file = open("hardlopers.txt","w")
		file.write(s,naam)
	