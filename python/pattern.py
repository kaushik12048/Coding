y=-1;m=15
x=input("enter no. of lines")
x=x/2+1
for i in range(0,x):
    y+=2;z=1;c=i;m-=1
    for sp in range(0,m):
        print " ",
    for j in range(0,y):
        print z,
        if(j<c):
            z+=1
        else:
            z-=1

            
    print

for i in range(x,0,-1):
    y-=2;z=1;c=i-2;m+=1
    for sp in range(0,m):
        print " ",
    for j in range(0,y):
        print z,
        if(j<c):
            z+=1
        else:
            z-=1

    print
    
    
    
