"""

      Money Sums

Task
Submit
Results
Statistics
Tests








CSES - Money Sums




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



You have n coins with certain values. Your task is to find all money sums you can create using these coins.
Input
The first input line has an integer n: the number of coins.
The next line has n integers x_1,x_2,\dots,x_n: the values of the coins.
Output
First print an integer k: the number of distinct money sums. After this, print all possible sums in increasing order.
Constraints

1 \le n \le 100
1 \le x_i \le 1000

Example
Input:
4
4 2 5 2

Output:
9
2 4 5 6 7 8 9 11 13
"""


def fn(i, sum, coins, hset, n):
    if i == n:
        hset.add(sum)
        return

    # incl
    fn(i + 1, sum + coins[i], coins, hset, n)
    # excl
    fn(i + 1, sum, coins, hset, n)

    return


n = int(input())
coins = list(map(int, input().split()))
hset = set()
fn(i=0, sum=0, coins=coins, hset=hset, n=n)
hset.discard(0)  # discard 0
lst = sorted(hset)
print(len(lst))
print(" ".join(map(str, lst)))
# print(*lst)
