
def reach_destination(distance,speed):
	divide = distance/speed
	return ("The train will be there in {} hours.".format((round(divide*2))/2))

print(reach_destination(95,22))