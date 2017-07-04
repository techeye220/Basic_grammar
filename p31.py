import math
def primer(n):
	for x in range(2,int(math.sqrt(n)+1)):
		if n%x==0:
			return 0
	return 1
y=2018
if primer(y)==0:
	print "No"
else:
	print "Yes"