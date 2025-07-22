"""
Counting Towers

Task
Submit
Results
Statistics
Tests








CSES - Counting Towers




addEventListener("DOMContentLoaded", function (e) {
    const mathElements = document.getElementsByClassName("math");
    const macros = {};
    for (let element of mathElements) {
        katex.render(element.textContent, element, {
            displayMode: element.classList.contains("math-display"),
            throwOnError: false,
            globalGroup: true,
            macros,
        });
    }
});


Time limit: 1.00 s
Memory limit: 512 MB



Your task is to build a tower whose width is 2 and height is n. You have an unlimited supply of blocks whose width and height are integers.
For example, here are some possible solutions for n=6:

Given n, how many different towers can you build? Mirrored and rotated towers are counted separately if they look different.
Input
The first input line contains an integer t: the number of tests.
After this, there are t lines, and each line contains an integer n: the height of the tower.
Output
For each test, print the number of towers modulo 10^9+7.
Constraints

1 \le t \le 100
1 \le n \le 10^6

Example
Input:
3
2
6
1337

Output:
8
2864
640403945
"""

# Need to debug this a little, logic is correct
# Refer to solve3 for working code

MOD = 10**9 + 7


def solve(n):
    if n == 1:
        return 2

    if n == 2:
        return 8

    # dp[i][j] = n(ways to have jth as curr state at ith intersection aka crossing)
    dp = [[0] * 9 for _ in range(n + 1)]

    # Using 1-based indexing for both row and col
    # Base Case: All states possible for 1st crossing
    for i in range(1, 8):
        dp[1][i] = 1

    # These sets are complementary
    cset1 = {1, 3, 4, 5, 6}
    cset2 = {2, 7, 8}
    pset1 = {1, 2, 4, 5, 6}
    pset2 = {3, 7, 8}

    # Recurring Case:
    for i in range(2, n + 1):
        for j in range(1, 8):
            if j in cset1:
                for pnum1 in pset1:
                    dp[i][j] += dp[i - 1][pnum1]
                    dp[i][j] %= MOD
            else:  # if j in cset2:
                for pnum2 in pset2:
                    dp[i][j] += dp[i - 1][pnum2]
                    dp[i][j] %= MOD

    return (dp[n][3] + dp[n][7]) % MOD


t = int(input())
a = []
for _ in range(t):
    d = solve(int(input()))
    a.append(d)
for i in range(t):
    print(a[i])
