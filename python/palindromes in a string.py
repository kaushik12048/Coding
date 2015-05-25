x=raw_input("enter a string")
x=x+" "
d=""
for i in range(0,len(x)):
    if(x[i]!=' '):
        d=d+x[i]
    else:
        m=""
        for j in range(0,len(d)):
            m=d[j]+m
        if(d==m):
            print d,
        d=""
        
        
