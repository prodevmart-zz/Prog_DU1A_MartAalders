import math
def hyp(a,b):
	c = math.sqrt(a) + math.sqrt(b)

	return c;

print(hyp(3,4))

def hello(name):
	return print("Welkom " + name)


hello("sdfsdf")

def rng(lijst):
	return max(lijst) - min(lijst) 

lijst1 = [1,2]
print(rng(lijst1));

def swapFS(a):
	b = a[1] 
	c = a[0]
	a[1] = c
	a[0] = b

	if len(a) >= 2:
		return a
still = [3,4,5,6,7]
print(swapFS(still))