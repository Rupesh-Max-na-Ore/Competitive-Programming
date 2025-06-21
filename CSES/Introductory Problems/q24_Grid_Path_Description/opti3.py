from typing import List

# Directions: right, down, left, up
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_valid(x: int, y: int, n: int) -> bool:
    return 0 <= x < n and 0 <= y < n

def count_unvisited_neighbors(x: int, y: int, vis: List[List[bool]], n: int) -> int:
    count = 0
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, n) and not vis[nx][ny]:
            count += 1
    return count

def dfs(x: int, y: int, step: int, total: int, vis: List[List[bool]], n: int) -> int:
    if x == n - 1 and y == 0:
        return int(step == total)

    forced_moves = []
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, n) and not vis[nx][ny]:
            neighbor_count = count_unvisited_neighbors(nx, ny, vis, n)
            if neighbor_count == 0:
                return 0  # dead-end
            elif neighbor_count == 1:
                forced_moves.append((nx, ny))

    vis[x][y] = True
    result = 0

    if forced_moves:
        # Only one move possible, must go there
        for nx, ny in forced_moves:
            result += dfs(nx, ny, step + 1, total, vis, n)
    else:
        # Normal DFS on all neighbors
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, n) and not vis[nx][ny]:
                result += dfs(nx, ny, step + 1, total, vis, n)

    vis[x][y] = False
    return result

def count_hamiltonian_paths(n: int) -> int:
    vis = [[False] * n for _ in range(n)]
    return dfs(0, 0, 1, n * n, vis, n)

# Try small n first (like n = 5)
n = 6
print(count_hamiltonian_paths(n))
