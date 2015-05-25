m=input("enter no. of rows")
n=input("enter no. of columns")
x=[[None]*n for i in range(m)]
for i in range(0,m):
    for j in range(0,n):
        x[i][j]=input("enter a number")
print x
