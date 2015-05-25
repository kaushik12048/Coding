a=input()
b=""
while(a!=0):
    if(a%2==0):
        b="0"+b
    else:
        b="1"+b
    a/=2
print int(b)
