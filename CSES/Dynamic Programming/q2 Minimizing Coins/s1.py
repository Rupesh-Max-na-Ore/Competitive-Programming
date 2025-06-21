"""
Minimizing Coins

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Minimizing Coins




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



Consider a money system consisting of n coins. Each coin has a positive integer value. Your task is to produce a sum of money x using the available coins in such a way that the number of coins is minimal.
For example, if the coins are \{1,5,7\} and the desired sum is 11, an optimal solution is 5+5+1 which requires 3 coins.
Input
The first input line has two integers n and x: the number of coins and the desired sum of money.
The second line has n distinct integers c_1,c_2,\dots,c_n: the value of each coin.
Output
Print one integer: the minimum number of coins. If it is not possible to produce the desired sum, print -1.
Constraints

1 \le n \le 100
1 \le x \le 10^6
1 \le c_i \le 10^6

Example
Input:
3 11
1 5 7

Output:
3

"""
import sys
sys.setrecursionlimit(10**7)

def solve(n,sum,curr):
    stp = 10**9 + 7
    dp=[10**9 + 7]*(sum+1)
    dp[0] = 0

    for i in range(len(curr)):
        stp= min(stp,pick(n, sum-curr[i], curr,1,dp))
    return stp if stp != 10**9 + 7 else -1

def pick(n,sum,curr,step,dp):
    if sum ==0:
        return step # 0 more coins needed to reach
    if sum < 0:
        return 10**9 + 8
    if dp[sum]!=10**9 + 7:
        return dp[sum]
    stp = 10**9 + 7
    for i in range(len(curr)):
        stp= min(stp,pick(n, sum-curr[i], curr,step+1,dp))
    dp[sum] = stp
    return stp if stp != 10**9 + 7 else 10**9 + 8

n,sum = map(int, input().split())
curr = list(map(int,input().split()))
print(solve(n,sum,curr))