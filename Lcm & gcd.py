def abc(a,b):
    l=max(a,b)
    s=min(a,b)
    t=l
    while(1):
        if t%s==0:
            return t
        t+=l
print(abc(7,5))

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
def lcm(a,b):
    return (a*b)//gcd(a,b)

print(lcm(5,7),gcd(5,7))

import math
print(math.gcd(5,7))
