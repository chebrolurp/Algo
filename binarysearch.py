import math
lis=[1,2,3,4,5,6,7,8,9]
n =int(raw_input())
def binarysearch(lis,n):
	while(len(lis)-1):
		mid = int(math.floor(len(lis)/2))
		if n == lis[mid]:
			return True
		else:
			if n < lis[mid] and len(lis) > 0:
				left = lis[slice(0,int(mid))]
				return binarysearch(left,n)
			elif n > lis[mid] and len(lis) > 0:
				right = lis[slice(int(mid),int(len(lis)))]
				return binarysearch(right,n)
	return False

print(binarysearch(lis,n))
