"""
CSES Problem Set
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

# Most recommended way

MOD = 10**9 + 7
MAX_N = 10**6 + 1


def precompute(n):
    dp = [[0, 0] for _ in range(n + 2)]
    dp[1][0] = 1  # Fully filled tower of height 1
    dp[1][1] = 1  # Partial fill (gap)

    for i in range(2, n + 1):
        dp[i][0] = (2 * dp[i - 1][0] + dp[i - 1][1]) % MOD
        dp[i][1] = (4 * dp[i - 1][1] + dp[i - 1][0]) % MOD

    return dp


solns_lookup = precompute(MAX_N)


def solve(dp, n):
    # Last transition empty above
    return (dp[n][0] + dp[n][1]) % MOD


t = int(input())
a = []
for _ in range(t):
    n = int(input())
    a.append(solve(solns_lookup, n))


for i in range(t):
    print(a[i])
