L = [1,2,10,13]
def GNC(l):     
	if len(L)<=2:
		return max(L)
	now=max(L[0],0)
	for i in range(2,len(L)):
		L[i]+=now
		now = max(L[i-1],now)
	return max(L)
print GNC(L)