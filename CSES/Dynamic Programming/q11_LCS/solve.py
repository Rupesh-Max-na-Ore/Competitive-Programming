"""
CSES Problem Set
      Longest Common Subsequence

Task
Submit
Results
Statistics
Tests








CSES - Longest Common Subsequence




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



Given two arrays of integers, find their longest common subsequence.
A subsequence is a sequence of array elements from left to right that can contain gaps. A common subsequence is a subsequence that appears in both arrays.
Input
The first line has two integers n and m: the sizes of the arrays.
The second line has n integers a_1,a_2,\dots,a_n: the contents of the first array.
The third line has m integers b_1,b_2,\dots,b_m: the contents of the second array.
Output
First print the length of the longest common subsequence.
After that, print an example of such a sequence. If there are several solutions, you can print any of them.
Constraints

1 \le n,m \le 1000
1 \le a_i, b_i \le 10^9

Example
Input:
8 6
3 1 3 2 7 4 8 2
6 5 1 2 3 4

Output:
3
1 2 4
"""

n, m = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a1[i - 1] == a2[j - 1]:
            dp[i][j] = 1 + dp[i - 1][j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

maxlen = dp[n][m]
print(maxlen)
# go thru to print lcs

leni = maxlen

i = n
j = m
ans = []
while leni > 0:
    if dp[i - 1][j] == leni:
        i -= 1
    elif dp[i][j - 1] == leni:
        j -= 1
    else:  # transition
        leni -= 1
        ans = [a1[i - 1]] + ans
        i -= 1
        j -= 1

print(*ans)
# print(" ".join(map(str, ans))) # Same as above
