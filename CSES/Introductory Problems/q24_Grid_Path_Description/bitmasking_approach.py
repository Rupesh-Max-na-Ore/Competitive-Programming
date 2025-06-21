from functools import lru_cache

N = 7
TOTAL_STEPS = 48
path = input().strip()  # Input: 48-character string

dx = [-1, 1, 0, 0]  # U, D, L, R
dy = [0, 0, -1, 1]
dir_idx = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

def bitpos(x, y):
    return x * N + y

@lru_cache(maxsize=None)
def dfs(x, y, step, visited_mask):
    if x == N - 1 and y == 0:
        return int(step == TOTAL_STEPS)
    if step >= TOTAL_STEPS:
        return 0

    move = path[step]
    res = 0

    for d in range(4):
        if move != '?' and dir_idx[move] != d:
            continue
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            pos = bitpos(nx, ny)
            if not (visited_mask & (1 << pos)):
                # Try moving to the cell
                res += dfs(nx, ny, step + 1, visited_mask | (1 << pos))
    return res

start_mask = 1 << bitpos(0, 0)
print(dfs(0, 0, 0, start_mask))
