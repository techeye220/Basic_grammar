def gdy(n,m):
	if n<m:
		t=n
		n=m
		m=t
	if m==0:
		return n
	else:
		return gdy(m,n%m)
L=[3,5,10]
max=1
for x in L:
	max=(max*x)/gdy(max,x)
print max