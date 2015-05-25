x=input("enter a number")
y=input("enter a number")
x=bin(x)
x=int(x[2:])
y=bin(y)
y=int(y[2:])
add=""
no=0
print "binary of 1st no.=",x
print "binary of 2nd no.=",y
if(y>x):
    y=y+x
    x=y-x
    y=y-x
    no=1
    
m=""
c=0

def call(x):
    c=0
    m=[]
    x=str(x)
    m.extend(x)
    x=int(x)
    i=0
    while(c==0):
        if(x%10==1):
            for j in range(0,i):
                m[len(m)-j-1]="1"
            c=1
        i+=1
        x/=10
        m[len(m)-i]="0"
    d=""
    for i in range(0,len(m)):
        d=d+m[i]
    return int(d)
while(x!=0 or y!=0):
    c=0
    if(x%10==0 and y%10==0):
        add="0"+add
    elif(x%10==0 and y%10==1):
        x=call(x/10)
        add="1"+add
        c=1
    elif(x%10==1 and y%10==0):
        add="1"+add
    elif(x%10==1 and y%10==1):
        add="0"+add
    if (c==0):
        x/=10
    y/=10
if no==1:
    print"binary subtraction="+"1"+add
else:
    print "binary subtraction=",add
sum1=0
i=0
if no==1:
    add=add[1:]
add=int(add)
while(add!=0):
    if(add%10==1):
        sum1=sum1+(2**i)
    add/=10
    i+=1
if no==1:
    print "-"+str(sum1)
else:
    print "decimal of binary subtraction=",sum1
