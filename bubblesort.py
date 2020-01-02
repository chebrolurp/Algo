list=[4,7,6,2,5,3,9,10,1,8,12]
swap = True
while(swap == True):
	swap = False
	for i in range(len(list)-1):
		if list[i]> list[i+1]:
			swap = True
			list[i],list[i+1] = list[i+1],list[i]
	
print(list)
