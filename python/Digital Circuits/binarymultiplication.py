x=input("enter a number")
y=input("enter a number")
x=bin(x)
x=int(x[2:])
y=bin(y)
y=int(y[2:])
d=""
l=[]
print "binary of 1st no.=",x
print "binary of 2nd no.=",y
def mul(a,b):
    e=""
    while(a!=0 or b!=0):
        p=a%10
        if(p==1 and b==1):
            e="1"+e
        else:
            e="0"+e
        a/=10
        if(len(str(a))==1 and a==0):
            b=0
           
    return e
k=0
while(len(str(y))!=1 or y!=0):
    d=mul(x,y%10)
    d=d+"0"*k
    l.append(d)
    y/=10
    k+=1
print l
x=int(l[0])
for i in range(1,len(l)):
    y=int(l[i])
    carry=0
    add=""
    while(x!=0 or y!=0):
        if((x%10==0 and y%10==0) and carry==0):
            carry=0
            add="0"+add
        elif((x%10==0 and y%10==0) and carry==1):
            carry=0
            add="1"+add
        elif(((x%10==0 and y%10==1) or (x%10==1 and y%10==0)) and carry==0):
            carry=0
            add="1"+add
        elif(((x%10==0 and y%10==1) or (x%10==1 and y%10==0)) and carry==1):
            carry=1
            add="0"+add
        elif((x%10==1 and y%10==1) and carry==0):
            carry=1
            add="0"+add
        elif((x%10==1 and y%10==1) and carry==1):
            carry=1
            add="1"+add
        x/=10
        y/=10
    if(carry==1):
        add="1"+add
    x=int(add)
i=0
print "binary multiplacation=",x
sum1=0
while(x!=0):
    if(x%10==1):
        sum1=sum1+(2**i)
    x/=10
    i+=1
print "decimal of multiplicated no.=",sum1
