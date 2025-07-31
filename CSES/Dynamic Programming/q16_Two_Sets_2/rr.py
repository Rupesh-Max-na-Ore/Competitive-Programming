"""
Two Sets II

Task
Submit
Results
Statistics
Tests







CSES - Two Sets II




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



Your task is to count the number of ways numbers 1,2,\ldots,n can be divided into two sets of equal sum.
For example, if n=7, there are four solutions:

\{1,3,4,6\} and \{2,5,7\}
\{1,2,5,6\} and \{3,4,7\}
\{1,2,4,7\} and \{3,5,6\}
\{1,6,7\} and \{2,3,4,5\}

Input
The only input line contains an integer n.
Output
Print the answer modulo 10^9+7.
Constraints

1 \le n \le 500

Example
Input:
7

Output:
4
"""

import sys

sys.setrecursionlimit(10**6)


n = int(input())
s1 = []
s2 = []


def fn(i):
    if i == n + 1:
        if sum(s1) == sum(s2):
            return 1
        # else
        return 0

    cnt = 0
    s1.append(i)
    cnt += fn(i + 1)
    s1.pop()
    s2.append(i)
    cnt += fn(i + 1)
    s2.pop()

    return cnt


print(int(fn(1) / 2))
