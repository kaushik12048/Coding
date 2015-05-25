dict={}
c=input()
d=input()
def func(a,b):
    global c;d
    if (a,b) in dict:
        return dict[a,b]
    elif(a!=b):
        if(a>b):
            a=a-b
        else:
            b=b-a
        func(a,b)
    else:
        dict[c,d]=a
    print dict
func(c,d)
print dict.values()
        
