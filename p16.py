 L = [2,-3,3,50]
 for i in range(1,len(L)):
     L[i]=max(L[i-2]+L[i],L[i-1])
 print L[len(L)-1]