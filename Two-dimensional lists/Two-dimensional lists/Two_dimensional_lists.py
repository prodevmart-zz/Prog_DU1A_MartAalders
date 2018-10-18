studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ] 

def gemiddelde_per_student(studentencijfers): 
	NewList = []
	nrows = len(studentencijfers)
	ncolums = len(studentencijfers[0])
	for student in range(nrows):
		for cijfers in range(ncolums):
			studentencijfers[student][cijfers] += 1
			return studentencijfers 	

print(gemiddelde_per_student(studentencijfers)) 

