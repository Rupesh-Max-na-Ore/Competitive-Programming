import sys

sys.setrecursionlimit(10000)


def dp(i, s):
    if i == n:
        return
    if (i, s) in memo:
        return
    memo.add((i, s))

    # Include coins[i]
    sums.add(s + coins[i])
    dp(i + 1, s + coins[i])

    # Exclude coins[i]
    dp(i + 1, s)


n = int(input())
coins = list(map(int, input().split()))
memo = set()
sums = set()
dp(0, 0)

ans = sorted(sums)
print(len(ans))
print(" ".join(map(str, ans)))
