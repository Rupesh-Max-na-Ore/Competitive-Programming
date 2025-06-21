path = input().strip()
grid = [[False for _ in range(7)] for _ in range(7)]
res = 0

# Directions in lexicographical order
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # R, L, D, U
DIR_LETTER = ['R', 'L', 'D', 'U']

def is_valid(x, y):
    return 0 <= x < 7 and 0 <= y < 7 and not grid[x][y]

def dead_end(x, y):
    cnt = 0
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny):
            cnt += 1
    return cnt == 0

def split_check(x, y):
    # If a path splits the grid vertically or horizontally with both sides blocked
    for a, b, c, d in [((x+1,y),(x-1,y),(x,y+1),(x,y-1)),
                       ((x,y+1),(x,y-1),(x+1,y),(x-1,y))]:
        if is_valid(*a) and is_valid(*b) and not is_valid(*c) and not is_valid(*d):
            return True
    return False

def dfs(x, y, i):
    global res
    if i == 48:
        if x == 6 and y == 0:
            res += 1
        return
    if x == 6 and y == 0:
        return  # early stop if we reach end before using all 48 steps

    if split_check(x, y):
        return

    grid[x][y] = True
    ch = path[i]

    for (dx, dy), dch in zip(DIRS, DIR_LETTER):
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny):
            if ch == '?' or ch == dch:
                dfs(nx, ny, i + 1)

    grid[x][y] = False

# Start DFS from (0,0)
dfs(0, 0, 0)
print(res)
