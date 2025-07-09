MOD = 10**9 + 7

def slv(n, sum, curr, dp):
    dp[0] = 1 # 1 way to reach 0 from 0

    for i in range(1, sum+1) :
        for coin in curr :
            if i - coin >= 0 :
                dp[i] += dp[i - coin] % MOD

    return dp[sum] % MOD

n, sum = map(int, input().split())
curr = list(map(int, input().split()))
res = slv(n, sum, curr, [0]*(sum+1))
print(res)