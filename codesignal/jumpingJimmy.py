#quesion from codesignal

def jumpingJimmy(tower, jumpHeight):
    sum = 0
    for i in tower:
    	if i <= jumpHeight:
    		sum += i
    	else:
    		break
    return sum

print(jumpingJimmy([3,1,2,5], 3))