x=raw_input()
x=x+" "
l=len(x)
a=[]
z=0
y=""
for i in range(0,l):
    if(x[i]!=' '):
        if(ord(x[i])>=65 and ord(x[i])<=90):
            z=ord(x[i])+32
            y=y+chr(z)
        elif(ord(x[i])>=97 and ord(x[i])<=122):
            z=ord(x[i])
            y=y+chr(z)
    else:
        a.append(y)
        y=""
print a
max1=0
high=""
for i in range(0,len(a)):
    c=0
    count=0
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            c=1
            break
    if(c==0):
        for m in range(0,len(a)):
            if(a[m]==a[i]):
                count+=1
        if(count>max1):
            high=a[i]
            max1=count
print high
print max1
            
            
        
                
