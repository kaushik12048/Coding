x=[]
n=input("no. of elements")
for i in range(0,n):
    x.append(input("enter a number"))
y=[x[i] for i in range(0,len(x)) for j in range(i+1,len(x)) if(x[i]==x[j] and x[i] not in x[:i])]
z=[x[i] for i in range(0,len(x)) if(x[i] not in y)]
y.extend(z)
print y
