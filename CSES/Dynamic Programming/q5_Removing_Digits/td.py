import sys
from functools import lru_cache
sys.setrecursionlimit(10**7)

@lru_cache(maxsize=None)
def fn(num):
    if num == 0:
        # If the number is already 0, no steps are needed
        return 0
    if num < 0:
        # return a big no. to ensure it is not counted as min_step update
        return 10**7
    
    steps = 0
    min_steps = 10**7 #large no. init
    # extract all digits of num variable and store them in a list
    digits = [int(d) for d in str(num)]
    # for each digit
    for digit in digits:
        if digit == 0:
            continue
        # count step as 1, and recursively call num - digit steps
        steps = 1 + fn(num - digit)
        min_steps = min(min_steps, steps)
    return min_steps
    

num = int(input())
res = fn(num)
print(res)