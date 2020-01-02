list=[4,7,6,5,3,9,10,23,8,21,0,31]
sorted_list = []
for i in range(len(list)):
	for j in range(i):
		if list[i]<list[j]:
			list.insert(j,list.pop(i))
			

print(list)
		
