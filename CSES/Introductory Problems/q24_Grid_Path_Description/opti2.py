from typing import List

# Four directions: right, down, left, up
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_valid(x: int, y: int, n: int) -> bool:
    return 0 <= x < n and 0 <= y < n

def count_unvisited_neighbors(x: int, y: int, vis: List[List[bool]], n: int) -> int:
    count = 0
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, n) and not vis[nx][ny]:
            count += 1
    return count

def is_dead_end(x: int, y: int, vis: List[List[bool]], n: int) -> bool:
    # After visiting (x, y), check if any neighboring unvisited cell is a dead end
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, n) and not vis[nx][ny]:
            if count_unvisited_neighbors(nx, ny, vis, n) == 0:
                return True
    return False

def dfs(x: int, y: int, steps: int, total: int, vis: List[List[bool]], n: int) -> int:
    if x == n - 1 and y == 0:
        return int(steps == total)

    if is_dead_end(x, y, vis, n):
        return 0

    vis[x][y] = True
    paths = 0

    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, n) and not vis[nx][ny]:
            paths += dfs(nx, ny, steps + 1, total, vis, n)

    vis[x][y] = False
    return paths

def count_hamiltonian_paths(n: int) -> int:
    vis = [[False] * n for _ in range(n)]
    vis[0][0] = True  # Start at top-left corner
    return dfs(0, 0, 1, n * n, vis, n)

# Example usage
n = 7
print(count_hamiltonian_paths(n))  # Try small n to test (like 5 or less)
