##linear search
##x=input("enter no. of elements")
##a=[]
##for i in range(0,x):
##    a.append(input("enter a number-->"))
##num=input("enter number to be searched")
##flag=-1
##for i in range(0,x):
##    if(a[i]==num):
##        flag=i+1
##        break
##if(flag==-1):
##    print "element not found"
##else:
##    print "element present at position",flag

## binary search without recursion
##x=input("enter no. of elements")
##a=[]
##for i in range(0,x):
##    a.append(input("enter a number-->"))
##num=input("enter number to be searched")
##l=0;u=len(a)-1;flag=-1
##while(l<=u and flag==-1):
##    mid=(l+u)/2
##    print mid
##    if(a[mid]==num):
##        flag=mid+1
##        break
##    else:
##        if(num<a[mid]):
##            u=mid-1
##        else:
##            l=mid+1
##if(flag!=-1):
##    print "number found at position",flag
##else:
##    print "number not found"


##binary search withrecursion
x=input("enter no. of elements")
a=[]
for i in range(0,x):
    a.append(input("enter a number-->"))
num=input("enter number to be searched")
l=0;u=len(a)-1
def binary(num,mid,low,high):
    mid=(low+high)/2
    if low>high:
        print "element not found"
        return -1
    if(a[mid]==num):
        print mid+1
    else:
        if(num<a[mid]):
            return binary(num,mid,low,mid-1)
        else:
            return binary(num,mid,mid+1,high)
binary(num,0,0,u)




