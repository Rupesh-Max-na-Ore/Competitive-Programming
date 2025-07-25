"""
CSES Problem Set
      Minimal Grid Path

Task
Submit
Results
Statistics
Tests








CSES - Minimal Grid Path




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



You are given an n \times n grid whose each square contains a letter.
You should move from the upper-left square to the lower-right square. You can only move right or down.
What is the lexicographically minimal string you can construct?
Input
The first line has an integer n: the size of the grid.
After this, there are n lines that describe the grid. Each line has n letters between A and Z.
Output
Print the lexicographically minimal string.
Constraints

1 \le n \le 3000

Example
Input:
4
AACA
BABC
ABDA
AACA

Output:
AAABACA
"""

import sys

sys.setrecursionlimit(1000000)


def fnc(i, j, n, grid):
    if i == n or j == n:
        return "Z"  # or "~" # some lexicographically heaviest character
    if i == n - 1 and j == n - 1:
        return grid[n - 1][n - 1]

    down = fnc(i + 1, j, n, grid)
    right = fnc(i, j + 1, n, grid)

    return grid[i][j] + min(down, right)


n = int(input())
grid = [["~"] * (n) for _ in range(n)]
# print("-------")
for i in range(n):
    ln = input().strip()
    for j in range(n):
        grid[i][j] = ln[j]
    # print(grid[i])


print(fnc(0, 0, n, grid))


# 1st attempt, didn't think much, but due to lexicographic sensitivity of sorting we can only construct paths forward dir not backward
# def fnc(i, j, grid):
#     # Base Case
#     if i == 0 and j == 0:
#         return grid[0][0]
#     if i < 0 or j < 0:
#         return ""

#     up = fnc(i - 1, j, grid)
#     left = fnc(i, j - 1, grid)

#     return grid[i][j] + min(up, left)


# n = int(input())
# grid = [["~"] * (n) for _ in range(n)]
# print("-------")
# for i in range(n):
#     ln = input().strip()
#     for j in range(n):
#         grid[i][j] = ln[j]
#     # print(grid[i])


# print(fnc(n - 1, n - 1, grid))
