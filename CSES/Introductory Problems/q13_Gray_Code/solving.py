"""
Gray Code

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Gray Code




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



A Gray code is a list of all 2^n bit strings of length n, where any two successive strings differ in exactly one bit (i.e., their Hamming distance is one).
Your task is to create a Gray code for a given length n.
Input
The only input line has an integer n.
Output
Print 2^n lines that describe the Gray code. You can print any valid solution.
Constraints

1 \le n \le 16

Example
Input:
2

Output:
00
01
11
10
"""

n = int(input())
#graycode
for i in range(1<<n):
    g_curr = i ^ (i >> 1)
    curr = format(g_curr, 'b').zfill(n)
    print(curr)
