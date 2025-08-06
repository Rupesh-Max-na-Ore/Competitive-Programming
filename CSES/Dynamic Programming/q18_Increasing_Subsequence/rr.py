"""
CSES Problem Set
                Increasing Subsequence

Task
Submit
Results
Statistics
Tests







CSES - Increasing Subsequence




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

You are given an array containing n integers. Your task is to determine the longest increasing subsequence in the array, i.e., the longest subsequence where every element is larger than the previous one.
A subsequence is a sequence that can be derived from the array by deleting some elements without changing the order of the remaining elements.
Input
The first line contains an integer n: the size of the array.
After this there are n integers x_1,x_2,\ldots,x_n: the contents of the array.
Output
Print the length of the longest increasing subsequence.
Constraints

1 \le n \le 2 \cdot 10^5
1 \le x_i \le 10^9

Example
Input:
8
7 3 5 3 6 2 9 8

Output:
4

"""

import sys

sys.setrecursionlimit(10000000)

n = int(input())
arr = list(map(int, input().split()))

from functools import lru_cache


def solve(n, arr):
    @lru_cache(maxsize=None)
    def fnc(i, par):
        if i == n:
            return 0

        pick, not_pick = 0, 0
        if par == -1 or par < arr[i]:
            pick = 1 + fnc(i + 1, arr[i])

        not_pick = fnc(i + 1, par)

        return max(pick, not_pick)

    print(fnc(0, -1))


solve(n, arr)
