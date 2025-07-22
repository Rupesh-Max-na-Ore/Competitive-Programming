# Not Recommended, Tried but some mistake I can't detect
# Will learn and redo this way

MOD = 10**9 + 7


def solve(n):
    if n == 1:
        return 1
    if n == 2:
        return 8

    prev2 = 1  # f(1)
    prev1 = 8  # f(2)

    for i in range(3, n + 1):
        curr = (4 * prev1 - prev2) % MOD
        prev2, prev1 = prev1, curr

    return prev1


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
