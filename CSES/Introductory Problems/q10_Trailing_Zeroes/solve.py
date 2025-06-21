"""
Trailing Zeros

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Trailing Zeros




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



Your task is to calculate the number of trailing zeros in the factorial n!.
For example, 20!=2432902008176640000 and it has 4 trailing zeros.
Input
The only input line has an integer n.
Output
Print the number of trailing zeros in n!.
Constraints

1 \le n \le 10^9

Example
Input:
20

Output:
4
"""

n = int(input())
k=n
tot = 0
pow = 5
#repeatedly divide n by 5 till n becomes 0 
while k != 0 :
    tot+= k//5
    k = k//5
print(tot)

# #or 
# #add divide by powers of 5 till it becomes more than n
# kn=n
# total = 0
# while pow <= n:
#     total+= kn//pow
#     pow*=5
# print(total)