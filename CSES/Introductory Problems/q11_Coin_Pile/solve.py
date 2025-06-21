"""
CSES Problem Set
      Coin Piles

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Coin Piles




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



You have two coin piles containing a and b coins. On each move, you can either remove one coin from the left pile and two coins from the right pile, or two coins from the left pile and one coin from the right pile.
Your task is to efficiently find out if you can empty both the piles.
Input
The first input line has an integer t: the number of tests.
After this, there are t lines, each of which has two integers a and b: the numbers of coins in the piles.
Output
For each test, print "YES" if you can empty the piles and "NO" otherwise.
Constraints

1 \le t \le 10^5
0 \le a, b \le 10^9

Example
Input:
3
2 1
2 2
3 3

Output:
YES
NO
YES
"""
##Testing, seems to work
# n=31
# m=32
# n=n%3
# m=m%3
# if(n==0 and m==0) or (n==1 and m==2) or (m==2 and n==1):
#     print("YES")
# else:
#     print("NO")

# # t = no. of test cases 
# t = int(input())
# for i in range(t):
#     n , m = map(int, input().split())
#     if not ((n==0 and m%3==0) or (m==0 and n%3==0)):
#         a = n%3
#         b = m%3
#         if(a==0 and b==0) or (a==1 and b==2) or (b==2 and a==1):
#             print("YES")
#         else:
#             print("NO")
#     else:
#         print("NO")

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if (a + b) % 3 == 0 and min(a, b) * 2 >= max(a, b):
        print("YES")
    else:
        print("NO")
