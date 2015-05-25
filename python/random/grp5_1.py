x=raw_input("enter string")
x=x+" "
z=[]
a=[]
b=""
for i in range(0,len(x)):
    if(x[i]!=' '):
        b=b+x[i]
    else:
        z.append(b)
        a.append(len(b))
        b=""
for i in range(0,len(z)):
    for j in range(i+1,len(z)):
        if(a[i]>a[j]):
            temp=z[i]
            z[i]=z[j]
            z[j]=temp
            tmp=a[i]
            a[i]=a[j]
            a[j]=tmp
print z
    
