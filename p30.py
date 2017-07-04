a=[]
n=52
for x in range(1,10):
    for y in range(10):
        for z in range(10):
            if x*2+y*2+z==n:
                a.append(x*10001+y*1010+z*100)
            if x*2+y*2+z*2==n:
                a.append(x*100001+y*10010+z*1100)
a.sort()
for i in a:
    print i