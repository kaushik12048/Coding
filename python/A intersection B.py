a=[]
x=input("enter no. of elements in list 1->")

b=[]
for m in range(0,x):
    a.append(input("enter a number"))
y=input("enter no. of elements in list 2->")

for n in range(0,y):
    b.append(input("enter a number"))
x=[a[i] for i in range(0,len(a)) for j in range(0,len(b)) if((a[i]==b[j]) and (a[i] not in a[:i]) and b[j] not in b[:j])]
print x
##print common
##b=[x for x in range(0,100) for i in range(2,x) if(x%i)==0]
##c=[x for x in range(0,100) if x not in b]
##print c
##gcd
##n1=input()
##n2=input()
##while(n1!=n2):
##    if(n1>n2):
##        n1=n1-n2
##    else:
##        n2=n2-n1
##print "gcd=",n1
##    
##def func(n,r):
##    y=n-r
##    sum1=1
##    sum2=1
##    sum3=1
##    for i in range(n,0,-1):
##        sum1=sum1*i
##    for i in range(y,0,-1):
##        sum2=sum2*i
##    for i in range(r,0,-1):
##        sum3=sum3*i
##    sum2=sum2*sum3
##    return sum1/sum2
##n=input("enter n ")
##y=input("enter r ")
##c=func(n,y)
##print c
