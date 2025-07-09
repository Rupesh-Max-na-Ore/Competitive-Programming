# Something wrong in this

import sys
sys.setrecursionlimit(10**7)

def solve(n,sum,curr):
    stp = 10**9 + 7 # Using a large number to represent infinity
    path = []

    dp = [-1] * (sum + 1)
    dp[0] = 0  # Base case: 0 coins needed to make sum 0


    for i in range(n):
        path.append(curr[i]) 
        stp= min(stp,pick(n, sum-curr[i], curr,1, path, dp))
        path.pop()
    print(path)  # Print the path taken for debugging
    dp[sum] = stp if (stp < 10**9 + 7) else -1
    return dp[sum]

def pick(n,sum,curr,step,path, dp):
    if sum == 0:
        print("Path taken:", path)
        return step # 0 more coins needed to reach
    if sum < 0:
        return 10**9 + 7
    if dp[sum] != -1:
        return dp[sum]

    stp = 10**9 + 7

    for i in range(n):
        path.append(curr[i])
        stp= min(stp,pick(n, sum-curr[i], curr,step+1, path, dp))
        path.pop()  # Remove the last coin added to the path
    
    dp[sum] = stp if stp != 10**9 + 7 else -1
    return dp[sum]

n,sum = map(int, input().split())
curr = list(map(int,input().split()))
print(solve(n,sum,curr))