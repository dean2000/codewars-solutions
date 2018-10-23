
array = [1,2,6,4,-6,9]

def positive_sum(arr):
    return (sum(num for num in arr if num >= 0))

print(positive_sum(array))

