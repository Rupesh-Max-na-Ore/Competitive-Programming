from functools import lru_cache

# The target grid size is 7x7 with 48 steps total
N = 7
TOTAL_STEPS = 48

# Movement vectors
dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
path = "??????R??????U??????????????????????????LD????D?"

# Direction character map to index
dir_idx = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# Precompute bit position for each cell
def bitpos(x, y):
    return x * N + y

@lru_cache(maxsize=None)
def dfs(x, y, step, visited_mask):
    if x == N - 1 and y == 0:
        return int(step == TOTAL_STEPS)

    if step >= TOTAL_STEPS:
        return 0

    res = 0
    move = path[step]
    for d, (dxi, dyi) in enumerate(zip(dx, dy)):
        if move != '?' and dir_idx[move] != d:
            continue
        nx, ny = x + dxi, y + dyi
        if 0 <= nx < N and 0 <= ny < N:
            pos = bitpos(nx, ny)
            if not (visited_mask & (1 << pos)):
                new_mask = visited_mask | (1 << pos)
                res += dfs(nx, ny, step + 1, new_mask)
    return res

# Start from (0, 0), step 0, mark it as visited
start_mask = 1 << bitpos(0, 0)
result = dfs(0, 0, 0, start_mask)
print(result)
