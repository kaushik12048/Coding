a=[6,1,5,2,4,9,3,7,231,44]
c=2
for i in range(len(a)-1,-1,-1):
    for j in range(len(a)-c,-1,-1):
        if(a[i]<a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
    c+=1
    print a
print a
a=[6,1,5,2,4,9,3,7,231,44]
for i in range(len(a)-1,-1,-1):
    Max=a[i]
    for j in range(i-1,-1,-1):
        if(a[j]>Max):
            Max=a[j]
            pos=j
            temp=a[i]
            a[i]=Max
            a[pos]=temp
    print a
print "final sorted list", a

a=[1,3,7,5,2,9,3,6,22,1]
