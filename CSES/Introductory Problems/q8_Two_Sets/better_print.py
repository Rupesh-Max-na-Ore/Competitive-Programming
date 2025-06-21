"""
Two Sets

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Two Sets




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



Your task is to divide the numbers 1,2,\ldots,n into two sets of equal sum.
Input
The only input line contains an integer n.
Output
Print "YES", if the division is possible, and "NO" otherwise.
After this, if the division is possible, print an example of how to create the sets. First, print the number of elements in the first set followed by the elements themselves in a separate line, and then, print the second set in a similar way.
Constraints

1 \le n \le 10^6

Example 1
Input:
7

Output:
YES
4
1 2 4 7
3
3 5 6
Example 2
Input:
6

Output:
NO
"""

def sets(n):
    sum = n*(n+1)//2
    if(sum % 2 == 1): 
        print("NO")
        return 
    l=1
    r=0 #random init
    f=[]
    s=[]
    if(n % 2 == 0):
        r = n
    else:
        r = n-1
    run = 1
    while(l<r): #stop when cross
        if(run % 2 == 1):
            f.append(l)
            f.append(r)
        else:
            s.append(l)
            s.append(r)
        l+=1
        r-=1
        run+=1
    if(n % 2 == 1):
        s.append(n)
    print("YES")
    print(len(f))
    print(' '.join(map(str, f)))
    print(len(s))
    print(' '.join(map(str, s)))

n = int(input())
sets(n)