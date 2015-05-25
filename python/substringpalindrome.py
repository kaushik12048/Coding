x=raw_input("enter a string")
a=[]
for i in range(0,len(x)):
    for j in range(len(x)-1,i,-1):
        if(x[i]==x[j]):
            d="";e=""
            for m in range(i,j+1):
                d=d+x[m]
            for n in range(i,j+1):
                e=x[n]+e
            if(d==e):
                a.append(e)
if len(a)>1:
    x=a[0]
    for i in range(1,len(a)):
        if(len(a[i])>len(x)):
            x=a[i]
    print x
elif len(a)==1:
    print a[0]
            
                
                
            
