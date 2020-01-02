lis = [3,7,2,5,8,9,1,4]
def quicksort(lis):
	if len(lis) < 2:
		return lis
	pivot = lis[-1]
	left = []
	right = []
	for i in range(len(lis)-1):
		if lis[i] < pivot:
			left.append(lis[i])
		else:
			right.append(lis[i])
	return quicksort(left)+[pivot]+quicksort(right)
#def stitch(left,pivot,right):
#	return left+[pivot]+right

print(quicksort(lis))
