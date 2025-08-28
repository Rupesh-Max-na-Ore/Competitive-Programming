"""
Counting Numbers

Task
Submit
Results
Statistics
Tests







CSES - Counting Numbers




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

Your task is to count the number of integers between a and b where no two adjacent digits are the same.
Input
The only input line has two integers a and b.
Output
Print one integer: the answer to the problem.
Constraints

0 \le a \le b \le 10^{18}

Example
Input:
123 321

Output:
171
"""

from functools import lru_cache


def count_valid(x: int) -> int:
    if x < 0:
        return 0
    digits = list(map(int, str(x)))
    n = len(digits)

    @lru_cache(None)
    def dp(pos: int, prev: int, tight: bool, leading: bool) -> int:
        if pos == n:
            return 0 if leading else 1  # valid if number formed

        limit = digits[pos] if tight else 9
        total = 0

        for d in range(0, limit + 1):
            if not leading and d == prev:
                continue
            total += dp(
                pos + 1,
                d if not leading else -1,
                tight and d == limit,
                leading and d == 0,
            )
        return total

    return dp(0, -1, True, True)


a, b = map(int, input().split())
print(count_valid(b) - count_valid(a - 1))
