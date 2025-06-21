from typing import List

def miss(n: int, a: List[int]):
    arr_sum = sum(a)
    summation = n*(n+1)//2 #error w/ '/' cuz python

    print(summation - arr_sum)

n = int(input())
lst = list(map(int, input().split()))
miss(n,lst)
