n=5
if n==1:
	print '0'
elif n==2:
	print '1'
elif n==3:
	print '2'
else:
	a=1
	b=2
	for i in range(4,n+1):
		c=a+b
		a=b
		b=c
	print b