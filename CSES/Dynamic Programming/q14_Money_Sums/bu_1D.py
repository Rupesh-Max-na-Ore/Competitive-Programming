n = int(input())
coins = list(map(int, input().split()))
max_sum = sum(coins)

possible = [False] * (max_sum + 1)
possible[0] = True

for coin in coins:
    for s in range(max_sum, coin - 1, -1):
        if possible[s - coin]:
            possible[s] = True

sums = [i for i in range(1, max_sum + 1) if possible[i]]
print(len(sums))
print(" ".join(map(str, sums)))
