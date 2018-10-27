infile = open('C:\\Users\Mart\Documents\GitHub\Prog_DU1A_MartAalders\Files lezen\kaartnummers.txt','r')
LineList = infile.readlines()
for lines in LineList:
	linesStrip = lines.strip()
	linesSplit = linesStrip.split(", ")
print("{} heeft kaartnummer {} Het hoogste is: {}".format(linesSplit[1],linesSplit[0],len(lines)))
