""" Program to display the new array contains the product of all other elements in the array"""

list = [2, 3, 5 ,4, 1]
list2 = []
var = 1
for l in list:
	for  i in range(0,5):
		if (l == list[i]):
			print "same"
		else:
			var = var*list[i]
	list2.append(var)
	var = 1

print list2