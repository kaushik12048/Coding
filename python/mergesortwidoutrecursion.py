a=[]
n=input("enter number of numbers")
temp=[]
for i in range(0,n):
    a.append(input("enter a number"))
print "values before the sort"
print
size=1
while(size<n):
    l1=0
    k=0
    while(l1+size < n):
        h1=l1+size-1
        l2=h1+1
        h2=l2+size-1
        if( h2>=n ) :
            h2=n-1
        i=l1
        j=l2
        while(i<=h1 and j<=h2):
            if( a[i] <= a[j] ):
                temp[k]=a[i]
                k+=1;i+=1
            else:
                temp[k]=a[j]
                k+=1;j+=1
        while(i<=h1):
            temp[k]=a[i]
            k+=1
            i+=1
        while(j<=h2):
            temp[k]=a[j]
            k+=1
            j+=1
        l1=h2+1
    size=size*2
print a
print temp
    
    
