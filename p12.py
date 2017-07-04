a=1
b=2
c=1
res = sorted([a,b,c])
if a+b>c and a+c>b and b+c>a:
	if res[2]*res[2]==res[0]*res[0]+res[1]*res[1]:
		print 'Z'
	elif res[2]*res[2]>res[0]*res[0]+res[1]*res[1]:
		print 'D'
	else:
		print 'R'
else:
	print 'W'