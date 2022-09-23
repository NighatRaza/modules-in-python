from this import d


def square(x):
    """returns square of a number"""
    return x**2
def power(x,pow):
    """exponential"""
    return x**pow
def table(x,times):
    """returns multiplication table"""
    for i in range(1,times+1):
        print(x,'*',i,'=',x*i)
def sqroot(x):
    """returns square root of a number"""
    return x**(1/2)
def divide(num,den):
    """returns quotient and remainder"""
    print('numerator is: ',num)
    print('denominator is: ',den)
    print('answer is:',num/den,'and remainder is:',num%den) 
    print('bye!')