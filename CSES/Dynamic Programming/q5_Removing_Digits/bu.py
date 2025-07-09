# dp[i] will store the minimum steps to reduce i to 0

def fn(num, dp):
    dp[0] = 0

    for i in range(1, num+1):
        for d in str(i):
            digit = int(d)
            if digit ==0:
                continue
            dp[i] = min(dp[i], 1 + dp[i - digit])

    # print(dp)
    return dp[num]

num = int(input())
res = fn(num, [10**7 for _ in range(num+1)])
print(res)