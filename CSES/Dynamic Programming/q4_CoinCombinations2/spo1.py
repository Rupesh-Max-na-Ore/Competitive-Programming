def countWays(n, tgt, coins):
    prev = [0] * (tgt + 1)
    prev[0] = 1  # One way to make sum 0

    # Lopp order needs go like this as we're following prev row capture to update curri
    for i in range(n):
        curri = [0] * (tgt + 1)
        curri[0] = 1
        for s in range(1, tgt + 1):
            incl = curri[s - coins[i]] if s >= coins[i] else 0
            excl = prev[s]
            curri[s] = incl + excl
        prev = curri  # Move to next coin
        print(prev)

    return prev[tgt]

# take i/p
n, tgt = map(int, input().split())
coins = list(map(int, input().split()))
print(countWays(n, tgt, coins))
