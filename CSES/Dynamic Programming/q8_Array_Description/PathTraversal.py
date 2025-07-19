"""
CSES Problem Set
      Array Description

Task
Submit
Results
Statistics
Tests








CSES - Array Description




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



You know that an array has n integers between 1 and  m, and the absolute difference between two adjacent values is at most 1.
Given a description of the array where some values may be unknown, your task is to count the number of arrays that match the description.
Input
The first input line has two integers n and m: the array size and the upper bound for each value.
The next line has n integers x_1,x_2,\dots,x_n: the contents of the array. Value 0 denotes an unknown value.
Output
Print one integer: the number of arrays modulo 10^9+7.
Constraints

1 \le n \le 10^5
1 \le m \le 100
0 \le x_i \le m

Example
Input:
3 5
2 0 2

Output:
3

Explanation: The arrays [2,1,2], [2,2,2] and [2,3,2] match the description.
"""

import sys

sys.setrecursionlimit(10**6)


MOD = 10**9 + 7


def pathTraversal(i, a, n, m, prev_nmbr):
    # Base case: completed the array
    if i == n:
        return 1

    # if abs(prev_nmbr - a[i]) > 1:
    #     return 0

    cnt = 0
    if a[i] != 0:
        # Value is fixed
        # cnt path iff its 1st number or abs diff is 1 or 0
        if prev_nmbr == -1 or abs(prev_nmbr - a[i]) <= 1:
            cnt += pathTraversal(i + 1, a, n, m, a[i])
    else:
        if prev_nmbr != -1:
            rng = [prev_nmbr]
            if prev_nmbr - 1 >= 1:
                rng.append(prev_nmbr - 1)
            if prev_nmbr + 1 <= m:
                rng.append(prev_nmbr + 1)
            for r in rng:
                cnt += pathTraversal(i + 1, a, n, m, r)
                cnt %= MOD
        else:  # if prev_nmbr == -1
            # First element can take any value
            for val in range(1, m + 1):
                cnt += pathTraversal(i + 1, a, n, m, val)
                cnt %= MOD

    return cnt % MOD


n, m = map(int, input().split())
a = list(map(int, input().split()))

print(pathTraversal(i=0, a=a, n=n, m=m, prev_nmbr=-1))


# 1st attempt, some mistakes
# def pathTraversal(i, a, n, m, prev_nmbr):
#     if i == n:
#         return 1

#     if abs(prev_nmbr - a[i]) > 1:
#         return 0

#     cnt = 0
#     if i != 0:
#         cnt += pathTraversal(i + 1, a, n, m, a[i])
#     else:
#         rng = [a[i - 1]]
#         if a[i - 1] - 1 >= 1:
#             rng.append(a[i - 1] - 1)
#         if a[i - 1] + 1 <= m:
#             rng.append(a[i - 1] + 1)
#         for r in rng:
#             cnt += pathTraversal(i + 1, a, n, m, r)

#     return cnt


# n, m = map(int, input().split())
# a = list(map(int, input().split()))

# print(pathTraversal(i=0, a=a, n=n, m=m, prev_nmbr=-1))

"""
MOD = 10**9 + 7

def countWays(i, prev, a, n, m):
    # Base case: completed the array
    if i == n:
        return 1

    total = 0
    if a[i] != 0:
        # Value is fixed
        if prev == -1 or abs(a[i] - prev) <= 1:
            total += countWays(i + 1, a[i], a, n, m)
    else:
        # Try all values between 1 and m
        for val in range(1, m + 1):
            if prev == -1 or abs(val - prev) <= 1:
                total += countWays(i + 1, val, a, n, m)
                total %= MOD

    return total % MOD

# Input reading
n, m = map(int, input().split())
a = list(map(int, input().split()))

# Initial call with no previous value
print(countWays(0, -1, a, n, m))

"""
