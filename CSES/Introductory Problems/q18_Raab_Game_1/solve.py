"""
Raab Game I

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Raab Game I




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



Consider a two player game where each player has n cards numbered 1,2,\dots,n. On each turn both players place one of their cards on the table. The player who placed the higher card gets one point. If the cards are equal, neither player gets a point. The game continues until all cards have been played.
You are given the number of cards n and the players' scores at the end of the game, a and b. Your task is to give an example of how the game could have played out.
Input
The first line contains one integer t: the number of tests.
Then there are t lines, each with three integers n, a and b.
Output
For each test case print YES if there is a game with the given outcome and NO otherwise.
If the answer is YES, print an example of one possible game. Print two lines representing the order in which the players place their cards. You can give any valid example.
Constraints

1 \le t \le 1000
1 \le n \le 100
0 \le a,b \le n

Example
Input:
5
4 1 2
2 0 1
3 0 0
2 1 1
4 4 1

Output:
YES
1 4 3 2
2 1 3 4
NO
YES
1 2 3
1 2 3
YES
1 2
2 1
NO
"""
def func(n,i,a,b,alst,blst,bset):
    if(i==n):
        if a==0 and b==0:
            return True
    p1 = i+1
    alst.append(p1)
    bsetlst = list(bset)
    for p2 in bsetlst:
        bset.remove(p2)
        blst.append(p2)
        if p1 == p2:
            t = func(n,i+1,a,b,alst,blst,bset)
        elif p1 > p2:
            t = func(n,i+1,a-1,b,alst,blst,bset)
        else:
            t = func(n,i+1,a,b-1,alst,blst,bset)
        if t==True:
            return True
        else:
            bset.add(p2)
            blst.pop()
    alst.pop()
    return False

def solve(n, a, b):
    alst,blst =[],[]
    bset = set()
    for j in range(1,n+1):
        bset.add(j)
    
    t = func(n,0,a,b,alst,blst,bset)
    if(t==True):
        print("YES")
        print(" ".join(map(str, alst)))
        print(" ".join(map(str, blst)))
    else:
        print("NO")

# solve(4,1,2)
t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    solve(n, a, b)
