##1st method

##a=input("no. of elements")
##b=[]
##for i in range(0,a):
##    b.append(input("enter a number"))
##c=[]
##for j in range(0,a):
##    count=0
##    for k in range(j+1,a):
##        if(b[j]==b[k]):
##            count+=1
##            break
##    if count==0:
##        c.append(b[j])
##print c



##2nd method
##x=[]
##n=input("no. of elements")
##for i in range(0,n):
##    x.append(input("enter a number"))
##y=[x[i] for i in range(0,len(x)) for j in range(i+1,len(x)) if(x[i]==x[j] and ((x[i] not in x[:i]) and x[j] not in x[i+1:j]))]
##
##z=[x[i] for i in range(0,len(x)) if(x[i] not in y)]
##y.extend(z)
##print y
