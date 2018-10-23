
def generate_hashtag(s):
	if len(s) < 140 and len(s) > 0:
		s = s.split(' ')
		for index1,name in enumerate(s):
			upper_case = ''.join([l for l in name[1:] if l.isupper()])
			lower_case = upper_case.lower()
			if upper_case:
				del s[index1]
			
				name = name.replace(upper_case,lower_case)
				s.insert(index1,name)
		if '' in s:
			del s[s.index(''):]
		s = '#' + ''.join(i[0].upper() + i[1:] for i in s)
		return s
	else:
		return False

print(generate_hashtag("codewars  is  nice"))



	

