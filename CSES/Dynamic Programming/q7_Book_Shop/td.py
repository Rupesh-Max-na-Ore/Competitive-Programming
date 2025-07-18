"""
Book Shop

Task
Submit
Results
Statistics
Tests








CSES - Book Shop




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



You are in a book shop which sells n different books. You know the price and number of pages of each book.
You have decided that the total price of your purchases will be at most x. What is the maximum number of pages you can buy? You can buy each book at most once.
Input
The first input line contains two integers n and x: the number of books and the maximum total price.
The next line contains n integers h_1,h_2,\ldots,h_n: the price of each book.
The last line contains n integers s_1,s_2,\ldots,s_n: the number of pages of each book.
Output
Print one integer: the maximum number of pages.
Constraints

1 \le n \le 1000
1 \le x \le 10^5
1 \le h_i, s_i \le 1000

Example
Input:
4 10
4 8 5 3
5 12 8 1

Output:
13

Explanation: You can buy books 1 and 3. Their price is 4+5=9 and the number of pages is 5+8=13.
"""


def fn(pgs, x, i, n, prices, pages, dp):
    # Base Case
    if i == n:
        return pgs
    # Memoized Case
    if dp[x][i] != -1:
        return dp[x][i]
    # Recurring Case
    incl = (
        fn(pgs + pages[i], x - prices[i], i + 1, n, prices, pages, dp)
        if x - prices[i] >= 0
        else 0
    )
    excl = fn(pgs, x, i + 1, n, prices, pages, dp)
    # Memoization - store the past calcs.
    dp[x][i] = max(incl, excl)
    return dp[x][i]


n, x = map(int, input().split())
prices = list(map(int, input().split()))
pages = list(map(int, input().split()))
print(fn(0, x, 0, n, prices, pages, [[-1 for _ in range(n + 1)] for _ in range(x + 1)]))
