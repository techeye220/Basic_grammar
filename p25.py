import math
a=3
b=1
if a<b:
	t=a
	a=b
	b=t
k=a-b
a=(int)(k*(1+5.0**0.5)/2.0)
if a==b:
	print "Loose"
else:
    print "Win"