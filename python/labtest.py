##def probability(n):
##    c=0
##    i=1
##    while i<7:
##        j=1
##        while j<7:
##            if (i+j)<=n:
##                c+=1
##            j+=1
##        i+=1
##    return c/36.0
##i=2            
##while(i<13):
##    x=probability(i)
##    print "probability that sum is less than or equal to",i,"is =",x
##    i+=1

##c=0
##d=0
##while(c==0 or d==0):
##    x=raw_input("enter a string->")
##    for character in x:
##        if character=='_':
##            c=1
##        if character=='s' or character=='S':
##            d=1
##def funcultimate(USER_STRING):
##    n=0
##    f=0
##    for i in range(0,len(USER_STRING)):
##        if(USER_STRING[f]=='s' or USER_STRING[f]=='S'):
##            n+=1
##        f+=1
##    for i in range(1,10):
##        if i%2==0:
##            continue
##        else:
##            print n,"*",i,"=",n*i
##x=raw_input("enter a string")
##funcultimate(x)

