num_int = None
odd_count = 0
sum = 0


while num_int != 0:
	num_str = input("Input an integer (0 terminates):")
	num_int = int(num_str)
	odd_count +=1
	sum += num_int
print("Er zijn " + str(odd_count) + " Getallen ingevoerd, de som is: "+ str(sum))
print()
