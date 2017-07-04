L =[-1,-2]
now=0
sum=0
t=0
for x in L:
	if x<0:
		t+=1
	now+=x
	if now>sum:
		sum=now
	if now<0:
		now=0
if t==len(L):
	L.sort()
	print L[0]
else:
	print sum