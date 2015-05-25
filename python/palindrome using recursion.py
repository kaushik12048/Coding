x=raw_input("enter a string")
def palindrome(y):
    if(len(y)==1 or len(y)==0):
        return True
    if(y[0]==y[len(y)-1]):
        return palindrome(y[1:len(y)-1])
    else:
        return False
print palindrome(x)

        
