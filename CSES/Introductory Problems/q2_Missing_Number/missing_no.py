"""

      
        
      
      
                RupeshMaxNaOre
        —
                        Dark mode
                Log out
              
    
  
  

  
    
      CSES Problem Set
      Missing Number

Task
Submit
Results
Analysis
Statistics
Tests
Queue

    
    
  

  

    
CSES - Missing Number




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



You are given all numbers between 1,2,\ldots,n except one. Your task is to find the missing number.
Input
The first input line contains an integer n.
The second line contains n-1 numbers. Each number is distinct and between 1 and n (inclusive).
Output
Print the missing number.
Constraints

2 \le n \le 2 \cdot 10^5

Example
Input:
5
2 3 1 5

Output:
4

"""

def missing(n : int, a : list[int]):
    lis = [False] * n
    for i in range(len(a)):
        lis[a[i]-1] = True

    for i in range(n):
        if(lis[i]==False):
            return print(i+1)
        
missing(5, [1,2,3,4])
missing(5, [1,2,3,5])