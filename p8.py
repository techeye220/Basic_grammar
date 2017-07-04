n=8
limit =[ 0,2,3,4,5,6,7,8]
cost=[1,2,3,4,5,6,7,8]
res=[]
for i in range(0,n):
    sum=0
    x=i
    flag=0
    for j in range(x,x+n):
    	sum=sum+limit[j%n]-cost[j%n]
    	if sum<0:
            flag=1
            break
    if flag==0:
    	res.append(i)
res.sort()
if len(res)==0:
	print '-1'
else:
    print res[0]