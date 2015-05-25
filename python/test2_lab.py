##lst=[]
##x=input("enter no. of elements")
##for i in range(0,x):
##    lst.append(input("enter a number"))
##
##def func(m):
##    if(len(m)==0):
##        return 0
##    else:
##        return (m[0]+func(m[1:]))
##print func(lst)
##def sort(m):
##    count=0
##    for i in range(0,len(m)):
##        for j in range(0,len(m)-i-1):
##            if(m[j]>m[j+1]):
##                temp=m[j]
##                m[j]=m[j+1]
##                m[j+1]=temp
##                count+=1
##    d=0
##    print "swaps=",count
##    for i in range(1,count+1):
##        if(count%i==0):
##            d=d+i
##    print d
##sort(lst)
