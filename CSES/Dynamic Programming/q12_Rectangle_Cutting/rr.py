"""
CSES Problem Set
      Rectangle Cutting

Task
Submit
Results
Statistics
Tests








CSES - Rectangle Cutting




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



Given an a \times b rectangle, your task is to cut it into squares. On each move you can select a rectangle and cut it into two rectangles in such a way that all side lengths remain integers. What is the minimum possible number of moves?
Input
The only input line has two integers a and b.
Output
Print one integer: the minimum number of moves.
Constraints

1 \le a,b \le 500

Example
Input:
3 5

Output:
3
"""

import sys

sys.setrecursionlimit(10**6)

a, b = map(int, input().split())


# Trying recursion
def fnc(a, b):
    if a == b:
        return 0

    ways = a * b

    # all hori cuts
    for i in range(1, b // 2):
        ways = min(ways, 1 + fnc(a, b - i) + fnc(a, i))
    # all vert cuts
    for i in range(1, a // 2):
        ways = min(ways, 1 + fnc(a - i, b) + fnc(i, b))
    return ways


print(fnc(a, b))
