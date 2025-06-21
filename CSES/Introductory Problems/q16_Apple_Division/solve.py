"""
Apple Division

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Apple Division




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



There are n apples with known weights. Your task is to divide the apples into two groups so that the difference between the weights of the groups is minimal.
Input
The first input line has an integer n: the number of apples.
The next line has n integers p_1,p_2,\dots,p_n: the weight of each apple.
Output
Print one integer: the minimum difference between the weights of the groups.
Constraints

1 \le n \le 20
1 \le p_i \le 10^9

Example
Input:
5
3 2 7 4 1

Output:
1

Explanation: Group 1 has weights 2, 3 and 4 (total weight 9), and group 2 has weights 1 and 7 (total weight 8).

"""
# def putt(i,n,lst,fst,scnd,maxdiff):
#     if(n==i):
#         diff = abs(sum(fst)-sum(scnd))
#         if diff < maxdiff:
#             maxdiff = diff
#             return
#     else:
#         fst.append(lst[i])
#         putt(i+1,n,lst,fst,scnd,maxdiff)
#         del fst[len(fst)-1]
#         scnd.append(lst[i])
#         putt(i+1,n,lst,fst,scnd,maxdiff)
#         del scnd[len(scnd)-1]
# def solve(n,lst):
#     fst=[]
#     scnd=[]
#     maxdiff=1000000001
#     putt(0,n,lst,fst,scnd,maxdiff)
#     return maxdiff
# n = int(input())
# lst = list(map(int, input().split()))
# print(solve(n, lst) )

def putt(i, n, lst, fst, scnd, maxdiff):
    if i == n:
        diff = abs(sum(fst) - sum(scnd))
        if diff < maxdiff[0]:
            maxdiff[0] = diff
        return
    fst.append(lst[i])
    putt(i + 1, n, lst, fst, scnd, maxdiff)
    fst.pop()
    scnd.append(lst[i])
    putt(i + 1, n, lst, fst, scnd, maxdiff)
    scnd.pop()

def solve(n, lst):
    fst = []
    scnd = []
    maxdiff = [10**18]  # Mutable list
    putt(0, n, lst, fst, scnd, maxdiff)
    return maxdiff[0]

# Input handling
n = int(input())
lst = list(map(int, input().split()))
print(solve(n, lst))
