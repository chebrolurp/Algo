import math
lists = [10,9,8,6,7,4,5,2,3,1,0]
def mergesort(lists):
	if len(lists) < 2:
		return lists
	mid = math.floor(len(lists)/2)
	left = lists[slice(0,int(mid))]
	right = lists[slice(int(mid),int(len(lists)))]
	return stitch(mergesort(left),mergesort(right))

def stitch(lef,righ):
	result = []
	while(len(lef) and len(righ)):
		if lef[0] < righ[0]:
			result.append(lef[0])
			lef.remove(lef[0])
		else:
			result.append(righ[0])
			righ.remove(righ[0])
	while(len(lef)):
		result.append(lef.pop(0))
	while(len(righ)):
		result.append(righ.pop(0))
	return result
print mergesort(lists)

