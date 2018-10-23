def find_uniq(arr):
    new_arr = ([''.join(list(set(i.lower()))) for i in arr])
    for item in set(new_arr):
    	if new_arr.count(item) == 1:
    		return arr[new_arr.index(item)]


print(find_uniq([ 'Aa', 'aaa', 'aaaaa',\
 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]))