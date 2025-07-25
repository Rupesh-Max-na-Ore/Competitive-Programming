"""
Grid Paths I

Task
Submit
Results
Statistics
Tests








CSES - Grid Paths I




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



Consider an n \times n grid whose squares may have traps. It is not allowed to move to a square with a trap.
Your task is to calculate the number of paths from the upper-left square to the lower-right square. You can only move right or down.
Input
The first input line has an integer n: the size of the grid.
After this, there are n lines that describe the grid. Each line has n characters: . denotes an empty cell, and * denotes a trap.
Output
Print the number of paths modulo 10^9+7.
Constraints

1 \le n \le 1000

Example
Input:
4
....
.*..
...*
*...

Output:
3
"""


def fn(x, y, a):
    # base case
    if x == 0 and y == 0:
        return 1

    #  recurring case
    res = 0
    res += fn(x - 1, y, a) if x - 1 >= 0 and a[x - 1][y] != "*" else 0
    res += fn(x, y - 1, a) if y - 1 >= 0 and a[x][y - 1] != "*" else 0

    return res


n = int(input())
a = [list(input().strip()) for _ in range(n)]

res = fn(n - 1, n - 1, a)
print(res)


"""
# Similarly
def fn(x, y, a):
    # Out of bounds
    if x < 0 or y < 0:
        return 0
    # Trap cell
    if a[x][y] == "*":
        return 0
    # Base case: start cell
    if x == 0 and y == 0:
        return 1

    # Recurring case
    return fn(x - 1, y, a) + fn(x, y - 1, a)

n = int(input())
a = [list(input().strip()) for _ in range(n)]

res = fn(n - 1, n - 1, a)
print(res)
"""
