def slv(n, sum, curr, dp):
    if sum < 0 :
        return 0
    if sum == 0 :
        return 1
    if dp[sum] != -1 :
        return dp[sum]
    
    ways = 0
    for coin in curr :
        ways += slv(n, sum - coin, curr, dp)
    
    dp[sum] = ways
    return ways

n, sum = map(int, input().split())
curr = list(map(int, input().split()))
print(slv(n, sum, curr, [-1]*(sum+1)))