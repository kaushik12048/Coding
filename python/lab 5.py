##print "enter the limits"
##def Range():
##    a=input("lower limit:")
##    b=input("upper limit:")
##    print "enter increment factor"
##    c=input()
##    shoplist=[]
##    if (a>b):
##        a=a+b
##        b=a-b
##        a=a-b
##    while(a<b):
##        y=str(a)
##        shoplist.append(y)
##        if(c>0):
##            a=a+c
##        else:
##            a=a-c
##    if c<0:
##        shoplist=shoplist[::-1]
##    return shoplist
##print Range()
##
##def Range():
##    a=raw_input("lower limit")
##    b=raw_input("upper limit")
##    c=input("enter increment factor")
##    shoplist=[]
##    y=ord(a)
##    z=ord(b)
##    if (y>z):
##        y=y+z
##        z=y-z
##        y=y-z
##    while(y<z):
##        
##        shoplist.append(chr(y))
##        if(c>0):
##            y=y+c
##        else:
##            y=y-c
##    if c<0:
##        shoplist=shoplist[::-1]
##    return shoplist
##print Range()
##
##def insertionsort():
##    j=input("enter how many nos. u want to enter:")
##    shoplist=[]
##    for i in range(0,j):
##        y=raw_input("enter a number:")
##        shoplist.append(y)
##    for i in range(1,j):
##        b=shoplist[i]
##        y=i-1
##        while(y>=0 and shoplist[y]>b):
##            shoplist[y+1]=shoplist[y]
##            y=y-1
##        shoplist[y+1]=b
##    print shoplist
##    
##insertionsort()

##
##def selectionsort():
##    z=input("enter how many nos. u want to enter:")
##    shoplist=[]
##    for i in range(0,z):
##        y=raw_input("enter a number:")
##        shoplist.append(y)
##    for x in range(0,z):
##        for y in range(x+1,z):
##            print y
##            if(shoplist[x]>shoplist[y]):
##                tmp=shoplist[x]
##                shoplist[x]=shoplist[y]
##                shoplist[y]=tmp
##    return shoplist
##print selectionsort()
##
