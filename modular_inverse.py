from datetime import datetime

def gcd(a, b):
    '''
    Calculate the Greatest Common Divisor of a and b.
    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    '''
    while b:
        a, b = b, a%b
    return a

def modular_inverse(p, q, m):
    '''
    Find "modulo inverse" of fraction
    p - numerator
    q - denominator
    m - modulo
    Use Fermat's little theorem
    '''
    q = q // gcd(p, q)
    return pow(q, -1, m)

start_time = datetime.now()

m = 1000000007
n = 2015
p = 1
q = pow(26, n//2, m)
print(modular_inverse(p, q, m))  # 680334730

print(datetime.now() - start_time)  # 0:00:00.000997 (17.08.2020)
