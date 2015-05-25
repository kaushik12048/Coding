x=input("enter a number")
y=input("enter a number")
x=bin(x)
x=int(x[2:])
y=bin(y)
y=int(y[2:])
carry=0
add=""
print "binary of 1st no.=",x
print "binary of 2nd no.=",y
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
print "binary addition=",add
sum1=0
i=0
add=int(add)
while(add!=0):
    if(add%10==1):
        sum1=sum1+(2**i)
    add/=10
    i+=1
print "decimal of added no.=",sum1

