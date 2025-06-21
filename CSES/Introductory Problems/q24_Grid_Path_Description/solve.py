"""
Grid Path Description

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Grid Path Description




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



There are 88418 paths in a 7 \times 7 grid from the upper-left square to the lower-left square. Each path corresponds to a 48-character description consisting of characters D (down), U (up), L (left) and R (right).
For example, the path

corresponds to the description DRURRRRRDDDLUULDDDLDRRURDDLLLLLURULURRUULDLLDDDD.
You are given a description of a path which may also contain characters ? (any direction). Your task is to calculate the number of paths that match the description.
Input
The only input line has a 48-character string of characters ?, D, U, L and R.
Output
Print one integer: the total number of paths.
Example
Input:
??????R??????U??????????????????????????LD????D?

Output:
201
"""
path = input().strip()
n = 7
grid = [[False] * n for _ in range(n)]
res = 0

# Directions: D, U, R, L
DIRS = {'D': (1, 0), 'U': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
DIR_ORDER = ['D', 'U', 'R', 'L']

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n and not grid[x][y]

def is_blocked(x, y):
    return not (0 <= x < n and 0 <= y < n) or grid[x][y]

def dfs(x, y, step):
    global res
    if x == 6 and y == 0:
        if step == 48:
            res += 1
        return
    if step >= 48:
        return

    # Prune: if stuck in a U-shape trap (3 sides blocked)
    if (is_blocked(x-1, y) and is_blocked(x+1, y) and not is_blocked(x, y-1) and not is_blocked(x, y+1)):
        return
    if (is_blocked(x, y-1) and is_blocked(x, y+1) and not is_blocked(x-1, y) and not is_blocked(x+1, y)):
        return

    grid[x][y] = True
    ch = path[step]

    for d in DIR_ORDER:
        if ch != '?' and ch != d:
            continue
        dx, dy = DIRS[d]
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny):
            dfs(nx, ny, step + 1)

    grid[x][y] = False  # backtrack

dfs(0, 0, 0)
print(res)

