"""

      
      
                RupeshMaxNaOre
        —
                        Dark mode
                Log out
              
    
  
  

  
    
      CSES Problem Set
      Weird Algorithm

Task
Submit
Results
Analysis
Statistics
Tests
Queue

    
    
  

  

    
CSES - Weird Algorithm




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



Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one. For example, the sequence for n=3 is as follows:
$$ 3 \rightarrow 10 \rightarrow 5 \rightarrow 16 \rightarrow 8 \rightarrow 4 \rightarrow 2 \rightarrow 1$$
Your task is to simulate the execution of the algorithm for a given value of n.
Input
The only input line contains an integer n.
Output
Print a line that contains all values of n during the algorithm.
Constraints

1 \le n \le 10^6

Example
Input:
3

Output:
3 10 5 16 8 4 2 1

"""

def Weird_Algo_(n):
    if(n<=0): 
        return "Wrong input"
    
    print(n)
    while(n != 1):
        if(n % 2 == 1): 
            n = n * 3 +1
        else: 
            n = n /2
        print(n)

Weird_Algo_(3)

#crct
def Weird_Algo(n):
    if n <= 0: 
        return "Wrong input"
    
    print(n, end=" ")
    while n != 1:
        if n % 2 == 1: 
            n = n * 3 + 1
        else: 
            n = n // 2
        print(n, end=" ")


Weird_Algo(3)