MOD = 10**9 + 7


def fn(n, a):
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if a[i][j] == "*":
                dp[i][j] = 0
            elif i == 0 and j == 0:
                dp[i][j] = 1
            else:
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
                dp[i][j] %= MOD
    return dp[n - 1][n - 1]


n = int(input())
a = [list(input().strip()) for _ in range(n)]
print(fn(n, a))

"""
# 1st attempt, some mistakes:

MOD = 10**9 + 7
 
 
def fn(n, a):
    dp = [[0 for _ in range(n)] for _ in range(n)]
 
    for y in range(n):
        for x in range(n):
            # Base case
            if x == 0 and y == 0:
                dp[x][y] = 1
            # Recursive case
            if x - 1 >= 0 and a[x - 1][y] != "*":
                dp[x][y] += dp[x - 1][y]
            if y - 1 >= 0 and a[x][y - 1] != "*":
                dp[x][y] += dp[x][y - 1]
            dp[x][y] %= MOD
    return dp[n - 1][n - 1]
 
 
n = int(input())
a = [list(input().strip()) for _ in range(n)]
print(fn(n, a))

Fails:
Test 11

Verdict: WRONG ANSWER
input
3
...
...
..*

correct output
0

user output
6

Test 13

Verdict: WRONG ANSWER
input
1
*

correct output
0

user output
1
"""
