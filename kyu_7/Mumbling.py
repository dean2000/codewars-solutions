#1.	Option 1 - not done

inp = "ZpglnRxqenU"

def accum(s):
	ls = (''.join(([x.lower()*(s.find(x)+1)+"-" for x in s])))
	return ls

#2. Option 2 - working solution

def accum(s):
	ls = []
	for index,letter in enumerate(s):
		ls.append(letter.upper())
		ls.append(letter.lower()*index)
		ls.append('-')
	return ''.join(l for l in ls[:-1])
	
print(accum(inp))

#3. Option 3 - clever solution

def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

print(accum(inp))
