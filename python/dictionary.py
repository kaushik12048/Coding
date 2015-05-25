##def rec(a):
##    if a==0 or a==1:
##        return a
##    else:
##        return rec(a-1)+rec(a-2)
##for i in range(0,10):
##    print rec(i),
##print 
##dict={}
##
##def mem(a):
##    if a==0 or a==1:
##        dict[a]=a
##    if a in dict:
##        return dict[a]
##    else:
##        dict[a]=mem(a-1)+mem(a-2)
##        return dict[a]
##for i in range(0,10):
##    print mem(i),
##    
a=raw_input("enter a string")
s=[]
e=[]
for i in range(0,len(a)):
    c=0
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            c=1
            break
    if(c==0 and a[i]!=' '):
        m=0
        for d in range(0,len(a)):
            if(a[d]==a[i]):
                m+=1
        s.append(a[i])
        e.append(m)
print s
print e
k=e[0]
f=s[0]
for i in range(1,len(e)):
    if(e[i]>k):
        k=e[i]
        f=s[i]
print k,f
        
        
                
