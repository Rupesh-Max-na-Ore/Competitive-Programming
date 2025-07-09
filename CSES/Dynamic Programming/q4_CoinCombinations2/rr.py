def ways(i, s, coins):
    if s == 0:
        return 1
    if i < 0 or s < 0:
        return 0
    # not pick ith coin and move to next coin or pick it and stay here 
    return ways(i - 1, s, coins) + ways(i, s - coins[i], coins)


n, sum = map(int, input().split())
curr = list(map(int, input().split()))
print(ways(n - 1, sum, curr))