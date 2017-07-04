a=2
b=7
x=2
y=4
def divide(a,b,c,d):
    result=""
    a=(a*pow(10,c-1,b))%b #小数点后一位的被除数
    print a
    for i in range(0,d-c+1):
        a=(a%b)*10
        result=result+str(a/b)
    return result
print divide(a,b,x,y)