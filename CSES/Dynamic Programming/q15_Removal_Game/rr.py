"""
Removal Game

Task
Submit
Results
Statistics
Tests








CSES - Removal Game




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



There is a list of n numbers and two players who move alternately. On each move, a player removes either the first or last number from the list, and their score increases by that number. Both players try to maximize their scores.
What is the maximum possible score for the first player when both players play optimally?
Input
The first input line contains an integer n: the size of the list.
The next line has n integers x_1,x_2,\ldots,x_n: the contents of the list.
Output
Print the maximum possible score for the first player.
Constraints

1 \le n \le 5000
-10^9 \le x_i \le 10^9

Example
Input:
4
4 5 1 3

Output:
8


Dynamic Programming...
Rectangle CuttingMinimal Grid PathMoney SumsRemoval GameTwo Sets IIMountain RangeIncreasing SubsequenceProjects...
    Your submissions
"""

import sys

sys.setrecursionlimit(10**6)
n = int(input())
a = list(map(int, input().split()))


def dp(i, j):
    if i == j:
        return a[i]

    # take max of Lth vs Rth
    ans = max(a[i] - dp(i + 1, j), a[j] - dp(i, j - 1))
    return ans


diffr = dp(0, n - 1)  # s1-s2
sm = sum(a)  # s1+s2
res = (sm + diffr) / 2  # s1
print(int(res))

# # 2nd atempt used greedy again
# def fn(l, r, player, p1_score, p2_score):
#     if l > r:
#         return p1_score

#     # p1_score_ = 0
#     # p2_score = 0
#     score = 0

#     if player == "p1":
#         # p1_score += max(a[l] + fn(l + 1, r, "p2"), a[r] + fn(l, r - 1, "p2"))
#         # return p1_score
#         score = max(
#             fn(l + 1, r, "p2", p1_score + a[l], p2_score),
#             fn(l, r - 1, "p2", p1_score + a[r], p2_score),
#         )
#         p1_score += score
#     elif player == "p2":
#         # p2_score += max(a[l] + fn(l + 1, r, "p1"), a[r] + fn(l, r - 1, "p1"))
#         # return p2_score
#         score = max(
#             fn(l + 1, r, "p1", p1_score, p2_score + a[l]),
#             fn(l, r - 1, "p1", p1_score, p2_score + a[r]),
#         )
#         p2_score += score

#     return p1_score


# print(fn(l=0, r=n - 1, player="p1", p1_score=0, p2_score=0))

# #1st attempt, used greedy
# def fn(l, r, player):
#     if l > r:
#         return 0

#     p1_score = 0
#     p2_score = 0

#     if player == "p1":
#         p1_score += max(a[l] + fn(l + 1, r, "p2"), a[r] + fn(l, r - 1, "p2"))
#         return p1_score
#     elif player == "p2":
#         p2_score += max(a[l] + fn(l + 1, r, "p1"), a[r] + fn(l, r - 1, "p1"))
#         return p2_score

#     return p1_score


# print(fn(l=0, r=n - 1, player="p1"))
