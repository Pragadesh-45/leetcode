a= [9,6,4,2,3,5,7,0,1]
a.sort()
for i in range(a[0],a[-1]):
	if i not in a:
		print(i)