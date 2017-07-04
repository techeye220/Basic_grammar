n=10
f = lambda x: all([x%c!=0 for c in range(2,x)])
p = [x for x in range(2,n) if f(x)]
sum=0
for x in range(0,len(p)):
	for y in range(x,len(p)):
		if p[x]+p[y]==n and p[x]!=p[y]:
			sum+=1
print sum