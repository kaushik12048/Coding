x=input("enter a no.")
x=bin(x)
x=int(x[2:])
print "binary of no.",x
d=""
while(x!=0):
    if(x%10==0):
        d="1"+d
    else:
        d="0"+d
    x/=10
print "one's complement",d
m=int(d)
k=""
c=0
s=0
if m==0:
    k="1"
while(m!=0):
    if(m%10==0 and c==0):
        k="1"
        s=0
    elif(m%10==1 and c==0):
        k="0"
        s=1
    if(m%10==0 and s==1 and c!=0):
        k="1"+k
        s=0
    elif(m%10==1 and s==1 and c!=0):
        k="0"+k
    else:
        if(c!=0):
            k=str(m%10)+k
    m/=10
    c+=1
    if(m==0 and s==1):
        k="1"+k
print "two's complement",k
        



