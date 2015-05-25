y=raw_input("enter a number in any base")
z=input("enter the base of the no.")
c=0
d=""
e=""
f=""
no=0
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
        no=1
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
if no==0:
    z=func(int(y))
else:
    z=m
    z=str(m)
y=input("enter the base to be converted to")
final=""
c=""
d=""
m=0
for i in range(0,len(z)):
    if(z[i]=="."):
        c=d
        m=1
        d=""
    else:
        d=d+z[i]
if(m==0):
    x=int(z)
else:
    x=int(c)
while(x>=y):
    k=x%y
    if(k>9):
        if(k==10):
            k="A"
        elif(k==11):
            k="B"
        elif(k==12):
            k="C"
        elif(k==13):
            k="D"
        elif(k==14):
            k="E"
        elif(k==15):
            k="F"
        final=k+final
    else:        
        final=str(k)+final
    x/=y
final=str(x)+final
if m==1:
    d="0."+d
    f1=""
    l=0
    k=float(d)
    
    for i in range(0,5):
        k=k*y
        if(k>=1):
            f1=f1+str(int(k))
            k=int(k)-k
        else:
            f1=f1+"0"
final=final+"."+f1        
print "no. converted to base",y,"=",final


