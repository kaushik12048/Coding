import time
x=input("enter no. of elements")
a=[]
for i in range(0,x):
    a.append(input("enter a number: "))
a.sort()
y=input("enter no. of elements")
b=[]
for j in range(0,y):
    b.append(input("enter a number"))
b.sort()
print a,b
i,j=0,0
m=len(a)
n=len(b)
c=[]
d=time.time()
while(i<m and j<n):
    if(a[i]<=b[j]):
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1
if(i<m):
    c+=a[i:]
elif(j<n):
    c+=b[j:]
print c
print time.time()-d
        
        
