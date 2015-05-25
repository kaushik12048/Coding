def fibonnaci_q1a(n):
    if n==1:
            return 0
    if n==2:
            return 1
    else :
            return fibonnaci_q1a(n-1)+fibonnaci_q1a(n-2)


dictionary_q1={}
def fibonnaci_q1b(n):
    if n in dictionary_q1:
            dictionary_q1[n]+=1
    else:
            dictionary_q1[n]=1
    if n==1:
            print dictionary_q1
            return 0
    if n==2:
            return 1
    else :
            return fibonnaci_q1b(n-1)+fibonnaci_q1b(n-2)
            
def factorial_q2(n):
    if n==1:
            return 1
    else:
            return n*factorial_q2(n-1)


def gcd_q3(a,b):
    if b==0:
            return a
    else:
            return gcd_q3(b,a%b)
            
dictionary_q4={}
def fibonnaci_q4(n):
    if n==1:
            return 0
    if n==2:
            return 1
    else:
            if n in dictionary_q4:
                    return dictionary_q4[n]
            else:
                    dictionary_q4[n]=fibonnaci_q4(n-1)+fibonnaci_q4(n-2)
                    return dictionary_q4[n]
                    
def printFactorialFirst_q7(n):
    for i in range(1,n+1):
            print "Factorial of",i,"is",factorial_q2(i)                    
def nPr_q8(n,r):
    return factorial_q2(n)/factorial_q2(n-r)
    
def nCr_q8(n,r):
    return factorial_q2(n)/(factorial_q2(n-r)*factorial_q2(r))
    
def asciiSum_q10(word):
    s=0
    for c in word:
            s+=ord(c)
    return s
    
def asciiDictionary_q10(listOfWords):
    asciiDict={}
    for word in listOfWords:
            asciiDict[word]=asciiSum_q10(word)
    return asciiDict


def lengthDictionary_q11(listOfWords):
    lengthDictionary={}
    for word in listOfWords:
            if len(word) in lengthDictionary:
                    lengthDictionary[len(word)].append(word)
            else:
                    lengthDictionary[len(word)]=[word]
    return lengthDictionary
import time
#print fibonnaci_q1a(3)
#print fibonnaci_q1b(10)
print factorial_q2(10)
print gcd_q3(4,11)
q4_start_memoize=time.time()
print fibonnaci_q4(10)
q4_end_memoize=time.time()
print "memoization took ",q4_end_memoize-q4_start_memoize, "s"
q4_start_no_memoize=time.time()
print fibonnaci_q1a(10)
q4_end_no_memoize=time.time()
print "Without memoization took ",q4_end_no_memoize-q4_start_no_memoize, "s"
printFactorialFirst_q7(10)
print "N P R  for N=",10,"and R=",5,nPr_q8(10,5)
print "N C R  for N=",10,"and R=",5,nCr_q8(10,5)


print "ASCII Dictionary :",asciiDictionary_q10(['alpha','beta','gamma','delta','ram','shyam','sita','gita'])
print "Length Dictionary :",lengthDictionary_q11(['alpha','beta','gamma','delta','ram','shyam','sita','gita'])
