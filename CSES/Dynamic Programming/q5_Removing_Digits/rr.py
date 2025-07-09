"""
CSES Problem Set
      Removing Digits

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Removing Digits




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



You are given an integer n. On each step, you may subtract one of the digits from the number.
How many steps are required to make the number equal to 0?
Input
The only input line has an integer n.
Output
Print one integer: the minimum number of steps.
Constraints

1 \le n \le 10^6

Example
Input:
27

Output:
5

Explanation: An optimal solution is 27 \rightarrow 20 \rightarrow 18 \rightarrow 10 \rightarrow 9 \rightarrow 0.
"""
import sys
sys.setrecursionlimit(10**7)

def fn(num):
    if num == 0:
        # If the number is already 0, no steps are needed
        return 0
    if num < 0:
        # return a big no. to ensure it is not counted as min_step update
        return 10**7
    
    steps = 0
    min_steps = 10**7 #large no. init
    # extract all digits of num variable and store them in a list
    digits = [int(d) for d in str(num)]
    # for each digit
    for digit in digits:
        if digit == 0:
            continue
        # count step as 1, and recursively call num - digit steps
        steps = 1 + fn(num - digit)
        min_steps = min(min_steps, steps)
    return min_steps
    

num = int(input())
res = fn(num)
print(res)