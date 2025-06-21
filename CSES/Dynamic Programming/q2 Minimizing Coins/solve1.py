# Top Down DP

import sys
sys.setrecursionlimit(10**7)

def solve(n, total, coins):
    dp = [-1] * (total + 1)

    def minCoins(x):
        if x == 0:
            return 0
        if x < 0:
            return float('inf')
        if dp[x] != -1:
            return dp[x]
        
        ans = float('inf')
        for c in coins:
            res = minCoins(x - c)
            if res != float('inf'):
                ans = min(ans, res + 1)
        
        dp[x] = ans
        return dp[x]

    result = minCoins(total)
    return result if result != float('inf') else -1

# extracting i/p
n, x = map(int, input().split())
coins = list(map(int, input().split()))
print(solve(n, x, coins))
