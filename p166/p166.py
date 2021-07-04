from multiprocessing import Pool
from collections import defaultdict
from itertools import product,repeat,combinations
from icecream import ic
from tqdm import tqdm
import numpy as np
import scipy


'''
A 4x4 grid is filled with digits d, 0 ≤ d ≤ 9.

It can be seen that in the grid

6 3 3 0
5 0 4 3
0 7 1 4
1 2 4 5

the sum of each row and each column has the value 12. Moreover the sum of each diagonal is also 12.

In how many ways can you fill a 4x4 grid with the digits d, 0 ≤ d ≤ 9 so that each row, each column, and both diagonals have the same sum?
'''

'''
observation 1: that the potential sum is quite limited (0 to 9+9+9+9=36)

observation 2: that given a sum, there are 'building blocks' for rows / columns / diagonals

                specifically, given say, 12, (6,3,3,0) is a building block; (5,0,4,3) is another one.

so the crux of the problem reduces to putting these building blocks together

but first, let's look at how many 'building blocks' are there for each potential sum
'''

tally=defaultdict(int)
lst=[list(range(10)) for _ in range(4)]
prod=product(*lst)
for a,b,c,d in tqdm(prod):
    tally[a+b+c+d]+=1
ic(tally)

'''
so... at most 700 'building blocks' for a potential sum

700**3 is less than 4 million. which means we can brute force from here.
'''

# first, generate 'building blocks'

buildingblocks=defaultdict(set)
lst=[list(range(10)) for _ in range(4)]
prod=product(*lst)
for a,b,c,d in tqdm(prod):
    buildingblocks[a+b+c+d].add((a,b,c,d))

# secondly, given a potential sum, count all answers

def checkdiagonals(rs,potentialsum):
    major,minor=0,0
    for i in range(4):
        major+=rs[i][i]
        minor+=rs[i][~i]
    return major==potentialsum and minor==potentialsum

def countanswers(potentialsum):
    count=0
    lst=[list(buildingblocks[potentialsum]) for _ in range(3)]
    prod=product(*lst)
    for r1,r2,r3 in tqdm(prod,desc=str(potentialsum)):
        r4=[potentialsum - re1 - re2 - re3 for re1,re2,re3 in zip(r1,r2,r3)]
        r4=tuple(r4)
        if r4 in buildingblocks[potentialsum] and checkdiagonals((r1,r2,r3,r4),potentialsum):
            count+=1
    return count

'''
without multiprocessing, this takes half an hour to complete on an i5 cpu

however, we can use multiprocessing to speed this up to under 10 minutes.

it's not hard to think of quadratic algorithms such as selecting pairs of two consecutive rows,

then do their respective column sum, do some clever joins (such as hashes) to speed the search

up. but to get accepted using an i5 cpu, cubic complexity is good enough. after all there is a

tradeoff between readability, reliability with time complexity.
'''

with Pool(5) as p:
    counts=p.map(countanswers,list(range(37)))
ic(sum(counts))
