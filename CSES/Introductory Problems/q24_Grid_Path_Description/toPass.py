import sys
sys.setrecursionlimit(10000)

# Directions encoded as (dr, dc): U, D, L, R
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Mapping from character to direction index
DIR_MAP = {'U': 0, 'D': 1, 'L': 2, 'R': 3, '?': -1}

# Global variables
visited = [[False] * 7 for _ in range(7)]
reserved = [-1] * 48
paths = 0

def is_trapped(r, c):
    """Prune paths that will surely fail due to being trapped"""
    # Vertical trap
    if (1 <= c <= 5 and not visited[r][c-1] and not visited[r][c+1]):
        if (r == 0 and visited[r+1][c]) or (r == 6 and visited[r-1][c]):
            return True
    # Horizontal trap
    if (1 <= r <= 5 and not visited[r-1][c] and not visited[r+1][c]):
        if (c == 0 and visited[r][c+1]) or (c == 6 and visited[r][c-1]):
            return True
    # Box traps
    if (1 <= r <= 5 and 1 <= c <= 5):
        if (visited[r+1][c] and visited[r-1][c] and not visited[r][c-1] and not visited[r][c+1]):
            return True
        if (visited[r][c+1] and visited[r][c-1] and not visited[r+1][c] and not visited[r-1][c]):
            return True
    return False

def solve(r, c, step):
    global paths

    # Reached end cell before 48 steps
    if r == 6 and c == 0:
        if step == 48:
            paths += 1
        return

    # If already visited or trapped, stop
    if visited[r][c] or is_trapped(r, c):
        return

    visited[r][c] = True

    if reserved[step] != -1:
        dr, dc = DIRS[reserved[step]]
        nr, nc = r + dr, c + dc
        if 0 <= nr < 7 and 0 <= nc < 7 and not visited[nr][nc]:
            solve(nr, nc, step + 1)
        visited[r][c] = False
        return

    for d in range(4):
        dr, dc = DIRS[d]
        nr, nc = r + dr, c + dc
        if 0 <= nr < 7 and 0 <= nc < 7 and not visited[nr][nc]:
            solve(nr, nc, step + 1)

    visited[r][c] = False

def main():
    global reserved
    s = input().strip()
    if len(s) != 48:
        print("Error: Input string must be exactly 48 characters long.")
        return

    reserved = [DIR_MAP[ch] for ch in s]
    solve(0, 0, 0)
    print(paths)

if __name__ == "__main__":
    main()
