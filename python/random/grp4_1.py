a=input("enter a number")
b=input("enter a number")
def binary(a):
    c="" 
    while(a!=0):
        if(a%2==0):
            c="0"+c
        else:
            c="1"+c
        a/=2
    return c
c=int((binary(a)))
d=int((binary(b)))
def func(x,y):
    if((len(str(x))==1 and x==0) and (len(str(y))==1 and y==0)):
        return 0
    else:
        e=(x%10)^(y%10)
        return func(x/10,y/10)*10+e
m=func(c,d)
print m
def decimal(x):
    c=0
    i=0
    while(x!=0):
        if(x%10!=0):
            c=c+pow(2,i)
        i+=1
        x/=10

    print c
decimal(m)
        
            

            
        
