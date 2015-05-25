from numpy import *
##a=zeros((3,3))  ##identity matrix of 3*3

##for i in range(0,3):
##    for j in range(0,3):
##        if(i==j):
##            a[i,j]=1
##        else:
##            a[i,j]=0
##print a
##i=input("number of rows")  ##inputting of the elements in an array
##j=input("number of columns")
##a = [[None]*j for z in range(i)] # Makes a matrix of dimensions i*j
##for x in range(i):
##    for y in range(j):
##        a[x][y]=input("enter a number")
##for x in range(i):
##    for y in range(j):
##        print a[x][y],
##    print
##num=input("enter  a number") ##counting occureneces of an element in an array
##c=0
##for x in range(0,i):
##    for y in range(0,j):
##        if(a[x][y]==num):
##            c+=1
##print c

##b=zeros((i,j))   ##printing array in upper triangular form
##for x in range(0,i):
##    for y in range(x,j):
##        b[x,y]=a[x,y]
##print b
##b=zeros((i,j))   ##printing array in lower triangular form
##for x in range(0,i):
##    for y in range(0,j-x):
##        b[x,y]=a[x,y]
##print b
##for x in range(0,i):  ##square of a matrix
##    for y in range(0,j):
##        a[x,y]=a[x,y]**2
##print a
# Difference between row-major and column-major

