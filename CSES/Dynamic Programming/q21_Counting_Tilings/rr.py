"""
Counting Tilings

Task
Submit
Results
Statistics
Tests







CSES - Counting Tilings




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

Your task is to count the number of ways you can fill an n \times m grid using 1 \times 2 and 2 \times 1 tiles.
Input
The only input line has two integers n and m.
Output
Print one integer: the number of ways modulo 10^9+7.
Constraints

1 \le n \le 10
1 \le m \le 1000

Example
Input:
4 7

Output:
781
"""

MOD = 10**9 + 7


def counting_tilings(n, m):
    # dp[col][mask] = number of ways to fill up to col-th column (from mth col) with mask state
    # mask represents which rows of the current column are already filled
    dp = [dict() for _ in range(m + 1)]
    dp[0][0] = 1  # base: no columns yet, empty state

    for col in range(m):
        for mask, ways in dp[col].items():
            # use DFS to fill next column given mask
            def dfs(row, curr_mask, next_mask):
                if row == n:
                    # reached end of column
                    dp[col + 1][next_mask] = (
                        dp[col + 1].get(next_mask, 0) + ways
                    ) % MOD
                    return
                if (curr_mask >> row) & 1:
                    # this row already filled
                    dfs(row + 1, curr_mask, next_mask)
                else:
                    # place vertical domino
                    dfs(row + 1, curr_mask, next_mask | (1 << row))
                    # place horizontal domino (if next row is free)
                    if row + 1 < n and not (curr_mask >> (row + 1)) & 1:
                        dfs(row + 2, curr_mask, next_mask)

            dfs(0, mask, 0)

    return dp[m].get(0, 0)  # only valid if last mask is empty


# # Example test
# if __name__ == "__main__":
#     n, m = 4, 3
#     print(counting_tilings(n, m))  # Expected output: 11


n, m = map(int, input().split())
print(counting_tilings(n, m))

# TLE on last 2 TCs in python

"""
Time complexity Analysis


say ith column had no position filled after filling i-1 th column.

now let us see number of possible config's for i+1 th column.



if jth position of i+1 th col is to be left empty then j+1th position will also
 be empty(as you will put a vertical tile at jth position of ith column). 



what is count of valid masks for i+1th column?
0 means a position is not filed(vertical tile at ith column), 1 means position is filed(horizontal tile at ith column)

f(N) = number of ways to fill N positions using 0s and 1s given that 0s occur in pairs.



At leftmost position if you fill in a 1 then you get f(N-1) ways and if you fill in a 0 then

immediate position to the right is also a 0 and you get f(N-2) ways.



f(N) = f(N-1) + f(N-2)



f(1) = 1, f(2) = 2



f(10) = 89



transition time is same as number of possible next masks.

if ith column had some positions filled then i+1th column would have even lesser possible next masks.

approximate upper bound on time complexity = 89*89*1000 ~ 10^7

"""
