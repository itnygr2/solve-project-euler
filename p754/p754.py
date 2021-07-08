from icecream import ic
import numpy as np
from tqdm import tqdm

# for 3, it's 4,5,7,8,10, so it's 10-3-10//3+1
# for 2, it's 3,5,7,9, so it's 10-2-10//2+1
# for 4, it's

def G(n):
    MOD=int(10**9+7)
    ans=1
    for i in range(2,n+1):
        freq=n-i-n//i+1
        ic(i,freq)
        #ans*=pow(i,freq,MOD)
        ans*=pow(i,freq)
    #return ans%MOD
    return ans

ic(G(10))
