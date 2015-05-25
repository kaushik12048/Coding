x=input("enter n")
def fib(n):
    if(n==0 or n==1):
        return n
    else:
        return fib(n-1)+fib(n-2)
y=fib(x-1)
print y
    
for i in range(1,11):
    print y,"*",i,"=",y*i
