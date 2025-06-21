"""
Mex Grid Construction

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Mex Grid Construction




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



Your task is to construct an n \times n grid where each square has the smallest nonnegative integer that does not appear to the left on the same row or above on the same column.
Input
The only line has an integer n.
Output
Print the grid according to the example.
Constraints

1 \le n \le 100

Example
Input:
5

Output:
0 1 2 3 4
1 0 3 2 5
2 3 0 1 6
3 2 1 0 7
4 5 6 7 0

"""
def solve(n):
    # grid = [[0]*n]*n wrong way makes reference to same list
    
    grid = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            used = set()

            # Elements to the left in the same row
            for k in range(j):
                used.add(grid[i][k])

            # Elements above in the same column
            for k in range(i):
                used.add(grid[k][j])

            # Find the MEX (smallest non-negative integer not in 'used')
            mex = 0
            while mex in used:
                mex += 1

            grid[i][j] = mex

    # Print the grid
    for row in grid:
        print(" ".join(map(str, row)))

# Input
n = int(input())
solve(n)
