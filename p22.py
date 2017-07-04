def Xbin(n,x):
	sum=0
	while n>0:
		sum+=n%x
		n/=x
	return sum
a=Xbin(n,10)
b=Xbin(n,16)
c=Xbin(n,12)
if a==b and b==c:
	print "Yes"
else:
	print "No"