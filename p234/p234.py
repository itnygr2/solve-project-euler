# there's too many writeups for this one
# basically just realize lps and ups don't change in (x^2,(x+1)^2)

from time import perf_counter
from math import ceil
from tqdm import tqdm
from icecream import ic
import sympy

start_time=perf_counter()

### setup ###

# ic(sympy.isprime(5)) #True

def lps(n):
    test=int(n**0.5)
    while test>0:
        if not sympy.isprime(test):
            test-=1
        else:
            return test
    return n+1 #something coprime to n that will fail the test

def ups(n):
    test=ceil(n**0.5)
    while test<=n:
        if not sympy.isprime(test):
            test+=1
        else:
            return test
    return n+1 #something coprime to n that will fail the test

# ic(lps(4),ups(4))
# ic(lps(1000),ups(1000))

def semidivisible(n):
    if n==2: return False
    conda=n%lps(n)==0
    condb=n%ups(n)==0
    return conda+condb==1

# ic(sum(i for i in range(1,16) if semidivisible(i)))
# ic(sum(i for i in range(1,1001) if semidivisible(i)))

### speedup ###

limit=999966663333

tally=0

def dividessum(d,a,b):
    '''sum numbers in (a,b) divides d'''
    b-=1
    b=b//d
    add=False
    a+=1
    if a%d:
        add=True
    a=a//d
    if add:
        a+=1
    res=d*(b-a+1)*(a+b)//2
    return res

for x in tqdm(range(2,ceil(limit**0.5))):
    # tally from x^2 to (x+1)^2
    l=lps(x**2)
    u=ups((x+1)**2)
    upperbound=min((x+1)**2,limit)
    # apply basic inclusion-exclusion
    tally+=dividessum(l,x**2,upperbound)
    tally+=dividessum(u,x**2,upperbound)
    tally-=dividessum(l*u,x**2,upperbound)
    tally-=dividessum(l*u,x**2,upperbound)

ic(tally)
ic(perf_counter()-start_time)
