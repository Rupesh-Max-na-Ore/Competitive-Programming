# 1 array space optimized solution
"""
We don't need curri
cuz we can just overwrite prev in a smart way
"""
def countWays(n, tgt, coins):
    prev = [0] * (tgt + 1)
    prev[0] = 1  # One way to make sum 0
    for s in range(coins[0], tgt+1, coins[0]):
        prev[s] = 1
    print(prev)
    for i in range(1, n):
        # curr[s] only depends on prev[s-coin[i]] and prev[s]
        # only frontward iteration from coin[i] to tgt works
        # backward only works if each coin type appears atmost once
        # but here it can appear infinite times till we exhaust sum s
        for s in range(coins[i], tgt + 1, +1):
            incl = prev[s - coins[i]] if s >= coins[i] else 0
            excl = prev[s]
            prev[s] = incl + excl
        print(prev)
    print("Final")
    print(prev)
    return prev[tgt]

# take i/p
n, tgt = map(int, input().split())
coins = list(map(int, input().split()))
print(countWays(n, tgt, coins))
