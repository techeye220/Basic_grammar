n=1
m=6
n=n+1
m=m+1
cnt = 1
dir = [[-1,2],[1,2],[-2,1],[2,1],[-2,-1],[2,-1],[-1,-2],[1,-2]]
map = [[0]*(m) for x in range(0,n)]
flag =[[0]*(m) for x in range(0,n)]
success = 0
step = [[0,0,0]] 
flag[0][0] = 1
while len(step)>0 and success==0:
	temp = step.pop()
	for i in range(0,8):
		ex = temp[0] + dir[i][0]
		ey = temp[1] + dir[i][1]
		if ex>=0 and ex<n and ey>=0 and ey<m and flag[ex][ey]==0:
			step.append([ex,ey,temp[2]+1])
			flag[ex][ey] = 1
	        if ex==n-1 and ey==m-1 :
	        	success = 1
	        	cnt = temp[2]+1
if success == 1:
	print cnt
else:
	print -1


