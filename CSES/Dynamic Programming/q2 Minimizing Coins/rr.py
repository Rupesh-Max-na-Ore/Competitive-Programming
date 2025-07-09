"""
Minimizing Coins


    
CSES - Minimizing Coins




Example
Input:
3 11
1 5 7

Output:
3


"""

import sys
sys.setrecursionlimit(10**7)

def solve(n,sum,curr):
    stp = 10**9 + 7 # Using a large number to represent infinity
    path = []

    for i in range(n):
        path.append(curr[i]) 
        stp= min(stp,pick(n, sum-curr[i], curr,1, path))
        path.pop()
    print(path)  # Print the path taken for debugging
    return stp if stp != 10**9 + 7 else -1

def pick(n,sum,curr,step,path):
    if sum == 0:
        print("Path taken:", path)
        return step # 0 more coins needed to reach
    if sum < 0:
        return 10**9 + 8
    

    stp = 10**9 + 7

    for i in range(n):
        path.append(curr[i])
        stp= min(stp,pick(n, sum-curr[i], curr,step+1, path))
        path.pop()  # Remove the last coin added to the path
    return stp if stp != 10**9 + 7 else 10**9 + 8

n,sum = map(int, input().split())
curr = list(map(int,input().split()))
print(solve(n,sum,curr))