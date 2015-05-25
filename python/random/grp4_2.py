x=raw_input("enter a string")
x=x+" "
z=""
b=""
for y in range(0,len(x)):
    if(x[y]==' '):
        z=z+b+" "
        b=""
    else:
        b=x[y]+b
print z
    
    
    
    
    
    
