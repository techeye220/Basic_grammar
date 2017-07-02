L = [4,2,1] 
UP = L[:]
UP.sort()
DOWN = UP[:]
DOWN.reverse()
if L==UP:
	print 'UP'
elif L==DOWN:
    print 'DOWN'
else:
    print 'WRONG'