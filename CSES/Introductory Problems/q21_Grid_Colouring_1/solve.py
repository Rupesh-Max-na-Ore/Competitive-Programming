"""
Grid Coloring I

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Grid Coloring I




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



You are given an n\times m grid where each cell contains one character A, B, C or D.
For each cell, you must change the character to A, B, C or D. The new character must be different from the old one.
Your task is to change the characters in every cell such that no two adjacent cells have the same character.
Input
The first line has two integers n and m: the number of rows and columns.
The next n lines each have m characters: the description of the grid.
Output
Print n lines each with m characters: the description of the final grid.
You may print any valid solution.
If no solution exists, just print IMPOSSIBLE.
Constraints

1 \le n, m \le 500

Example
Input:
3 4
AAAA
BBBB
CCDD

Output:
CDCD
DCDC
ABAB
"""

from collections import deque
import copy
def gcolor(n,m,g):
    q = deque()
    q.append((0,0))
    nbrd = [(0,1), (1,0), (0,-1), (-1,0)]
    # color = copy.deepcopy(g)
    color = [['' for _ in range(m)] for _ in range(n)]
    visited = set()
    while q:
        y,x=q.popleft()
        if (y,x) in visited:
            continue
        valid = {'A','B','C','D'}
        #valid.remove(color[y][x])
        valid.remove(grid[y][x])
        for dx,dy in nbrd:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n:
                if (ny,nx) not in visited:
                    q.append((ny,nx))
                if color[ny][nx] in valid:
                    if color[ny][nx]!='':
                        valid.remove(color[ny][nx])
        color[y][x]=valid.pop()
        visited.add((y,x))
    for row in color:
        print("".join(map(str,row)))

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

gcolor(n, m, grid)

# from collections import deque

# def gcolor(n, m, grid):
#     q = deque()
#     q.append((0, 0))
    
#     nbrd = [(0,1), (1,0), (0,-1), (-1,0)]  # Right, Down, Left, Up
    
#     color = [['' for _ in range(m)] for _ in range(n)]
#     visited = set()
    
#     while q:
#         y, x = q.popleft()
#         if (y, x) in visited:
#             continue

#         # Step 1: get valid colors (≠ original and ≠ adjacent)
#         valid = {'A', 'B', 'C', 'D'}
        
#         # Remove original character
#         if grid[y][x] in valid:
#             valid.remove(grid[y][x])
        
#         # Remove colors used by already-colored neighbors
#         for dy, dx in nbrd:
#             ny, nx = y + dy, x + dx
#             if 0 <= ny < n and 0 <= nx < m:
#                 if color[ny][nx] in valid:
#                     valid.remove(color[ny][nx])
#                 # Enqueue neighbor if not visited
#                 if (ny, nx) not in visited:
#                     q.append((ny, nx))
        
#         if not valid:
#             print("IMPOSSIBLE")
#             return
        
#         color[y][x] = valid.pop()
#         visited.add((y, x))
    
#     for row in color:
#         print("".join(row))


# # Input reading
# n, m = map(int, input().split())
# grid = [list(input().strip()) for _ in range(n)]
# gcolor(n, m, grid)
