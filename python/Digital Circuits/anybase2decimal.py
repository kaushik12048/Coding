y=raw_input("enter a number in any base")
z=input("enter the base of the no.")
c=0
d=""
e=""
f=""
def func(a):
    i=0
    if c!=0:
        i=-1
    
    str1=0
    while(a!=0):
        if(a%10==0):
            str1=str1+0
        else:
            str1=float((a%10)*(z**i))+str1
        a/=10
        if c==0:
            i+=1
        else:
            i-=1
    return str(str1)
for i in range(0,len(y)):
    if(y[i]=="."):
        e=func(int(d))
        c=i
        d=""
    else:
        d=d+y[i]
m=0
if c==0:
    print "DECIMAL NO.=",func(int(y))
else:
    d=d[::-1]
    f=func(int(d))
    m=float(e)+float(f)
    print "DECIMAL NO.=",m           
