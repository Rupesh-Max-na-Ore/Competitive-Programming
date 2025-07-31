"""
Mountain Range

Task
Submit
Results
Statistics
Tests







CSES - Mountain Range




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



There are n mountains in a row, each with a specific height. You begin your hang gliding route from some mountain.
You can glide from mountain a to mountain b if mountain a is taller than mountain b and all mountains between a and b.
What is the maximum number of mountains you can visit on your route?
Input
The first line has an integer n: the number of mountains.
The next line has n integers h_1, h_2,\dots, h_n: the heights of the mountains.
Output:
Print one integer: the maximum number of mountains.
Constraints

1\le n \le 2 \cdot 10^5
1\le h_i \le 10^9

Example
Input:
10
20 15 17 35 25 40 12 19 13 12

Output:
5
"""

# Given how I understood the problem, this is correct formulation, but I misunderstood it at first
import sys

sys.setrecursionlimit(10**7)

n = int(input())
a = list(map(int, input().split()))

# maxi = 1
curr = 1
pillar = a[0]


def fn(i, n, curr, pillar):
    if i == n:
        return curr

    if a[i] < pillar:
        return fn(i + 1, n, curr + 1, pillar)
    else:
        return max(curr, fn(i + 1, n, 1, a[i]))


# def fn(i, n, curr, pillar):
#     if i == n:
#         return curr

#     if a[i] < pillar:
#         return max(curr, fn(i + 1, n, curr + 1, pillar))
#     else:
#         return max(curr, fn(i + 1, n, 1, a[i]))


# def fn(i, n, maxi, curr, pillar):
#     if i == n:
#         return curr

#     if a[i] < pillar:
#         curr += 1
#     else:
#         # maxi = max(maxi, curr)
#         curr = 1
#         pillar = a[i]

#     return max(maxi, fn(i + 1, n, maxi, curr, pillar))


print(fn(1, n, curr, pillar))
