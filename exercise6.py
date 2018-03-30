# James Ward March 2018

# A function to calculate factorials

def factorial (n):
    nfact = 1
    while n >= 1:
        nfact = nfact * n
        n = n - 1
    return nfact
    
print ("The factorial of 5 is", factorial(5))

print ("The factorial of 7 is", factorial(7))

print ("The factorial of 10 is", factorial(10))