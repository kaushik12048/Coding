##count sort
##x=input("enter number of elements-->")
##a=[]
##for i in range(0,x):
##    a.append(input("enter a number"))
##def quick_srt(array,low,n):
##    lo=low
##    hi=n
##    if (lo >= n):
##      return
##    mid = array[(lo + hi) / 2]
##    while (lo < hi):
##      while (lo<hi and array[lo] < mid):
##          lo+=1
##      while (lo<hi and array[hi] > mid):
##          hi-=1
##      if (lo < hi):
##          T = array[lo]
##          array[lo] = array[hi]
##          array[hi] = T
##    if (hi < lo):
##      T = hi
##      hi = lo
##      lo = T
##    quick_srt(array, low, lo)
##    quick_srt(array,lo+1,n)
##quick_srt(a,0,len(a)-1)
##print "sorted array-->"
##for i in range(0,x):
##    print a[i]," ",
##    


##insertion sort
##x=input("enter number of elements-->")
##a=[]
##for i in range(0,x):
##    a.append(input("enter a number"))
##l=len(a)
##for x in range(0,l):
##    b=a[x];c=x-1
##    while(c>=0 and a[c]>b):
##        a[c+1]=a[c]
##        c-=1
##    a[c+1]=b
##for x in range(0,l):
##    print a[x],

##selection sort
##x=input("enter number of elements-->")
##a=[]
##for i in range(0,x):
##    a.append(input("enter a number"))
##l=len(a)
##for x in range(0,l):
##    b=a[x];c=x
##    for y in range(x+1,l):
##        if(a[y]<b):
##            b=a[y]
##            c=y
##    a[c]=a[x]
##    a[x]=b
##for x in range(0,l):
##    print a[x],
##another method
##for x in range(0,l):
##    for y in range(x+1,l):
##        if(a[x]>a[y]):
##            temp=a[y]
##            a[y]=a[x]
##            a[x]=temp
##print a

##bubble sort
##x=input("enter number of numbers-->")
##a=[]
##for i in range(0,x):
##    a.append(input("enter a number"))
##l=len(a)
##for x in range(0,l):
##    for y in range(0,l-1-x):
##        if(a[y]>a[y+1]):
##            z=a[y]
##            a[y]=a[y+1]
##            a[y+1]=z
##for x in range(0,l):
##    print a[x],
##
##count sort            
##x=input("number of elements")
##b=[]
##for i in range(0,x):
##    b.append(input("enter a number"))
##c=0
##for j in range(0,x):
##    if(c<b[j]):
##        c=b[j]
##    
##def counting_sort(array, maxval):
##    m = maxval + 1
##    count = [0] *m  ##init with zeros
##    for a in array:
##        count[a] += 1             # count occurences
##    i = 0
##    for a in range(m):            # emit
##        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
##            array[i] = a
##            i += 1
##    return array
## 
##print counting_sort(b,c)

##merge sort
##a=[]
##n=input("enter number of elements")
##
##for i in range(0,n):
##    a.append(input("enter a number"))
##print "values before the sort"
##for i in range(0,len(a)):
##    print a[i]," ",
##print
##def mergesort_srt(a,lo,n):
##    low=lo
##    high=n
##    if low>=high:
##        return 
##    middle=(low+high)/2
##    mergesort_srt(a,low,middle)
##    mergesort_srt(a,middle+1,high)
##    end_low=middle
##    start_high=middle+1
##    while((lo<=end_low) and (start_high<=high)):
##        if(a[low]<a[start_high]):
##            low+=1
##        else:
##            Temp=a[start_high]
##            for k in range(start_high-1,low-1,-1):
##                a[k+1]=a[k]
##            a[low]=Temp
##            low+=1
##            end_low+=1
##            start_high+=1
##mergesort_srt(a,0,len(a)-1)
##
##print "values after the sort"
##for i in range(0,len(a)):
##    print a[i]," ",
    
