#recurion
def factorial(n):
    if n==1 or  n==1: #base condition
        return 1 or 0
    return n*factorial(n-1)
print(factorial(5))

#add n natural numbers    #n(n+1)/2
def sumnatural(n):
    if n==1:
        return 1
    return n+sumnatural(n-1)
print(sumnatural(10))

def sumnatural(n):
    if n==2:
        return 2
    return n+sumnatural(n-2)
print(sumnatural(10))

def sumnatural1(n):
    if n%2==0:
        if n==2:
            return 2
        return n+sumnatural1(n-2)
    else:
        if n==1:
            return 1
        return n+sumnatural1(n-2)
print(sumnatural1(9))
