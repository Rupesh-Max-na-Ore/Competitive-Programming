def pick(n, sum, curr, memo):
    if sum == 0:
        return 0
    if sum < 0:
        return int(1e9)
    if sum in memo:
        return memo[sum]

    min_coins = int(1e9)
    for i in range(n):
        min_coins = min(min_coins, 1 + pick(n, sum - curr[i], curr, memo))
    memo[sum] = min_coins
    return min_coins

n, x = map(int, input().split())
curr = list(map(int, input().split()))
res = pick(n, x, curr, {})
print(res if res < int(1e9) else -1)

# min_coin == steps, dp == memo