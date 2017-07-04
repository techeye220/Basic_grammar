a=100
b=100
flag=0
for i in range(-10000,10001):
	if i*(a-i)==b:
		print "Yes"
		flag=1
		break
if flag==0:
	print "No"