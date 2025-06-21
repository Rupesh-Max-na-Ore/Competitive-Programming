# Optimized version of the grid path description problem with additional forced move rule

path = "??????R??????U??????????????????????????LD????D?"

grid = [[False for _ in range(7)] for _ in range(7)]
res = 0

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # R, L, D, U
DIR_LETTER = ['R', 'L', 'D', 'U']

def is_valid(x, y):
    return 0 <= x < 7 and 0 <= y < 7 and not grid[x][y]

def dfs(x, y, i):
    global res
    if i == 48:
        if x == 6 and y == 0:
            res += 1
        return
    if x == 6 and y == 0:
        return

    # Pruning: avoid "trapping" by disallowing grid splits
    if (
        (not is_valid(x + 1, y) and not is_valid(x - 1, y) and is_valid(x, y + 1) and is_valid(x, y - 1)) or
        (not is_valid(x, y + 1) and not is_valid(x, y - 1) and is_valid(x + 1, y) and is_valid(x - 1, y))
    ):
        return

    grid[x][y] = True
    ch = path[i]

    for (dx, dy), dch in zip(DIRS, DIR_LETTER):
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny) and (ch == '?' or ch == dch):
            dfs(nx, ny, i + 1)

    grid[x][y] = False

dfs(0, 0, 0)
res
