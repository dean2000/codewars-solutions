import math

name = "deanmarkin"

def matrixfy(st):
	if not st: return "name must be at least one letter"
	divider = 1
	while (len(st) / divider) > divider:
		divider += 1
	splited = list(list(st[i:i+divider])for i in range(0,len(st),divider))
	while len(splited[-1]) < divider:
		splited[-1] = splited[-1] + ['.']
	while len(splited) < divider:
		splited.append(['.']*divider)
	return splited
		
print(matrixfy(name))

