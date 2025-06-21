"""
Increasing Array

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Increasing Array




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



You are given an array of n integers. You want to modify the array so that it is increasing, i.e., every element is at least as large as the previous element.
On each move, you may increase the value of any element by one. What is the minimum number of moves required?
Input
The first input line contains an integer n: the size of the array.
Then, the second line contains n integers x_1,x_2,\ldots,x_n: the contents of the array.
Output
Print the minimum number of moves.
Constraints

1 \le n \le 2 \cdot 10^5
1 \le x_i \le 10^9

Example
Input:
5
3 2 5 1 7

Output:
5
"""

from typing import List

# def incr_arr(n:int,a:List[int]):
#     tot,move,l=0,0,0
#     r = 1
#     while(r<n):
#         if not (a[l]<=a[r]+move):
#             move+=1
#         else:
#             tot+=move
#             move=0
#             l=r
#             r+=1
#     return tot

# n = int(input())
# a = list(map(int, input().split()))
# print(incr_arr(n,a))
def incr_arr(n:int,a:List[int]):
    tot,l=0,0
    r=1
    while(r<n):
        if(a[l]>a[r]):
            move = a[l]-a[r]
            tot+= move
            a[r] = a[l]
        l=r
        r+=1
    return tot


n = int(input())
a = list(map(int, input().split()))
print(incr_arr(n,a))