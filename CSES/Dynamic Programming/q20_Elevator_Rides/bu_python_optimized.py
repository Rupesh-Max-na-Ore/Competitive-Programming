n, lt = map(int, input().split())
wt = list(map(int, input().split()))

dp = [(10**9, 10**9)] * (1 << n)
dp[0] = (1, 0)

for subset in range(1, 1 << n):
    best = (10**9, 10**9)
    for ltb in range(n):
        if subset & (1 << ltb):
            cr, clowt = dp[subset ^ (1 << ltb)]
            if clowt + wt[ltb] <= lt:
                new_state = (cr, clowt + wt[ltb])
            else:
                new_state = (cr + 1, wt[ltb])
            if new_state < best:
                best = new_state
    dp[subset] = best

print(dp[(1 << n) - 1][0])
