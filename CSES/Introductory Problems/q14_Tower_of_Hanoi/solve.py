"""
Tower of Hanoi

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Tower of Hanoi




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



The Tower of Hanoi game consists of three stacks (left, middle and right) and n round disks of different sizes. Initially, the left stack has all the disks, in increasing order of size from top to bottom.
The goal is to move all the disks to the right stack using the middle stack. On each move you can move the uppermost disk from a stack to another stack. In addition, it is not allowed to place a larger disk on a smaller disk.
Your task is to find a solution that minimizes the number of moves.
Input
The only input line has an integer n: the number of disks.
Output
First print an integer k: the minimum number of moves.
After this, print k lines that describe the moves. Each line has two integers a and b: you move a disk from stack a to stack b.
Constraints

1 \le n \le 16

Example
Input:
2

Output:
3
1 2
1 3
2 3

"""

# def toh(n, a, b, c):
#     if n == 0:
#         return
#     toh(n-1,a,c,b)
#     src = ord(a) - ord('a') + 1
#     dest = ord(c) - ord('a') + 1
#     print(f"{src} {dest}")
#     toh(n-1,b,a,c)

# def solve(n):
#     toh(n, 'a', 'b', 'c')

# n = int(input())
# solve(n)

"""
a: src
b: aux
c: dest
toh(n, a, b, c) == move n-1 at top of a to b
                    move a to c (largest/bottomest disk)
                   move n-1 at top of b to c

                   do above until n==0
"""
def toh(n, a, b, c):
    if n == 0:
        return
    toh(n-1,a,c,b)
    print(f"{a} {c}")
    toh(n-1,b,a,c)

def solve(n):
    cnt = 2**n -1 #total moves for any n
    print(cnt)
    toh(n, '1', '2', '3')

n = int(input())
solve(n)
