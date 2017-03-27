list = [2,2,2,4,1,1,3,4,4,4,5,8,8]
#list = [4,4,4,4,4,4,4,4]
list2 = []
counter = 0

value = list[1]
for l in list:
	#print l
	if(l == value):
		counter = counter + 1
	else :
		list2.append(counter)
		list2.append(value)
		value = l
		counter = 1
list2.append(counter)
list2.append(value)

print list2