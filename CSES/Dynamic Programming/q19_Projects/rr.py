"""

                Projects

Task
Submit
Results
Statistics
Tests







CSES - Projects




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

There are n projects you can attend. For each project, you know its starting and ending days and the amount of money you would get as reward. You can only attend one project during a day.
What is the maximum amount of money you can earn?
Input
The first input line contains an integer n: the number of projects.
After this, there are n lines. Each such line has three integers a_i, b_i, and p_i: the starting day, the ending day, and the reward.
Output
Print one integer: the maximum amount of money you can earn.
Constraints

1 \le n \le 2 \cdot 10^5
1 \le a_i \le b_i \le 10^9
1 \le p_i \le 10^9

Example
Input:
4
2 4 4
3 6 6
6 8 2
5 7 3

Output:
7
"""

import sys

sys.setrecursionlimit(10000000)

n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))
    #  print(mat[i])

booked = set()


def fn(i, booked):
    if i == n:
        return 0

    excl = 0 + fn(i + 1, booked)

    to_chk = [_ for _ in range(mat[i][0], mat[i][1] + 1, +1)]

    for tc in to_chk:
        if tc in booked:
            return excl

    # booked.add(_ for _ in to_chk) #this is wrong
    booked.update(to_chk)
    incl = mat[i][2] + fn(i + 1, booked)
    # Backtrack (undo booking)
    booked.difference_update(to_chk)
    return max(excl, incl)


print(fn(0, booked))
