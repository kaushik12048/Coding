a=[]
x=input("enter no. of elements")
for i in range(0,x):
    a.append(input("enter a number"))
for i in range(0,x):
    b=a[i];c=i-1
    while(c>=0 and a[c]>b):
        a[c+1]=a[c]
        c-=1
    a[c+1]=b
print a
m=[a[i] for i in range(len(a)) if a[i] not in a[i+1:]]
d=len(m)
for j in range(0,x+d-2):
    if((a[j]!=a[j+1] and a[j]!=0) or (j==0 and a[j]!=a[j+1])):
        a.append(0)
        for m in range(len(a)-1,j,-1):
            a[m]=a[m-1]
        a[j+1]=0
a.append(0)
print a
c=0
m=input("enter a number")
for i in range(0,len(a)):
    if(c==1):
        break
    if(a[i]==m):
        for j in range(i,len(a)):
            if(a[j]==0):
                a[j]=m
                c=1
                break
print a
            
