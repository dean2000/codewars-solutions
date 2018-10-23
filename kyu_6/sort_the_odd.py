
array = [5,3,2,8,1,4]

def sort_array(source_array):
	new_array = sorted(list(filter(lambda x: x%2 != 0, source_array)))
	for num in source_array:
		if num not in new_array:
			new_array.insert(source_array.index(num),num)
	return new_array

print(sort_array(array))
# help(list.insert)
