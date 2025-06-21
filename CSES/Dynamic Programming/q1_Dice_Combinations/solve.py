"""
Dice Combinations

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Dice Combinations




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



Your task is to count the number of ways to construct sum n by throwing a dice one or more times. Each throw produces an outcome between 1 and  6.
For example, if n=3, there are 4 ways:

1+1+1
1+2
2+1
3

Input
The only input line has an integer n.
Output
Print the number of ways modulo 10^9+7.
Constraints

1 \le n \le 10^6

Example
Input:
3

Output:
4
"""
import sys
sys.setrecursionlimit(10**7)  # Ensure enough recursion depth

MOD = 10**9 + 7
def solve(n):
    a = [-1] *(n+1)
    a[0] = 1
    pick =0
    for i in range (1,7):
        pick += dice(n-i,a) % MOD

    a[n] = pick % MOD

    return a[n]

def dice(n,a):
    if n==0:
        return 1
    if n<0:
        return 0
    if a[n] != -1:
        return a[n]
    pick =0
    for i in range (1,7):
        pick += dice(n-i,a) % MOD

    
    a[n] = pick % MOD

    return a[n]

n = int(input())

print(solve(n))