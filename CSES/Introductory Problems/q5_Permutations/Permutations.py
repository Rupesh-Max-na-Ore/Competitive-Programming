"""
Permutations

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Permutations




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



A permutation of integers 1,2,\ldots,n is called beautiful if there are no adjacent elements whose difference is 1.
Given n, construct a beautiful permutation if such a permutation exists.
Input
The only input line contains an integer n.
Output
Print a beautiful permutation of integers 1,2,\ldots,n. If there are several solutions, you may print any of them. If there are no solutions, print "NO SOLUTION".
Constraints

1 \le n \le 10^6

Example 1
Input:
5

Output:
4 2 5 3 1
Example 2
Input:
3

Output:
NO SOLUTION

"""
#passes TCs upto n = 10, then RecursionError: maximum recursion depth exceeded
def perm(n, st, a, indx):
    if indx == n:
        if beaut(n, a):
            return a[:]
        return None  # No valid permutation found here
    
    
    for i in range(1,n+1):
        if(i in st):
            continue
        #else
        st.add(i)
        a[indx] = i
        res = perm(n,st,a,indx+1)
        if res:
            return res
        st.remove(i) #Backtrack

    return None # No valid permutation from this path

def beaut(n, a):
    for i in range(0, n - 1):
        if abs(a[i+1] - a[i]) == 1:
            return False
    return True

n = int(input())
a = [0] * n
used = set()
res = perm(n, used, a, 0)

if res:
    print(*res)
else:
    print("NO SOLUTION")