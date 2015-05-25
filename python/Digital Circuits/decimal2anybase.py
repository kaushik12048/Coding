z=raw_input("enter a number")
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
f1=""
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

