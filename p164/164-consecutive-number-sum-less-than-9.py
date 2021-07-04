from functools import lru_cache
from icecream import ic
import numpy as np
from tqdm import tqdm


# How many 20 digit numbers n (without any leading zero) exist such that no three consecutive digits of n have a sum greater than 9?


# dp

@lru_cache(None)
def dp(place,prevs):
    if place==19:
        ans=0
        for d in range(10):
            if sum(prevs)+d>9:
                continue
            ans+=1
        return ans
    elif place==0:
        return sum(dp(1,d) for d in range(1,10)) #no leading zero allowed
    elif place==1:
        ans=0
        for d in range(10):
            if prevs+d>9:
                continue
            ans+=dp(2,(prevs,d))
        return ans
    else:
        ans=0
        for d in range(10):
            if sum(prevs)+d>9:
                continue
            ans+=dp(place+1,(prevs[-1],d))
        return ans

ic(dp(0,None))
