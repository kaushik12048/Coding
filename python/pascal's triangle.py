def tri(myrange):
    trianglevar = [[1]]
    for i in range(1, myrange):
        tempvar = [1]
        for n in range(0, i-1):
            tempvar.append(trianglevar[i-1][n]+trianglevar[i-1][n+1])
        tempvar.append(1)
        trianglevar.append(tempvar)
    return trianglevar

def menu():
    n=25
    for i in tri(int(raw_input("Please enter the height of the triangle: "))):
        print " "*n,
        for j in range(0,len(i)):
            print str(i[j])+" ",
        n-=2
        print
    print '\n'
    var = raw_input("Would you like to create another triangle? (y/n): ")
    if var == "y":
        menu()

    else:
        print "exit"
menu()
