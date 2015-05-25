class stringerror(Exception):
    pass 
def exceptin():
    try:
        a=input("enter a number")
        b=input("enter a number")
        if(b==1):
            raise stringerror
        else:
            print a/b 
    except ZeroDivisionError:
        print "Error:Division by 0"
    except stringerror:
        print "division by 1"
    except:
        print "other errors"
    else:
        print "no errors"
    finally:
        print "process completed"
exceptin()
