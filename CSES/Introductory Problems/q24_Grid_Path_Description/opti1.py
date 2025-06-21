def fn(r, c, step, stop, vis, n):
    # Base case: if we reach the target at the final step
    if r == n - 1 and c == 0:
        return 1 if step == stop else 0

    total = 0
    vis[r][c] = True

    # Movement directions: Down, Up, Right, Left
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and not vis[nr][nc]:
            total += fn(nr, nc, step + 1, stop, vis, n)

    vis[r][c] = False  # Backtrack
    return total

def hamiltonian_paths_with_symmetry(n):
    vis = [[False for _ in range(n)] for _ in range(n)]

    total_paths = 0

    # Only explore one direction first (down or right), not both.
    vis[0][0] = True  # mark starting cell

    if n > 1:
        # First move Down (1,0)
        total_paths += fn(1, 0, 1, n * n - 1, vis, n)

        # First move Right (0,1)
        total_paths += fn(0, 1, 1, n * n - 1, vis, n)

    return total_paths

# Run the function
n = int(input("Enter n (<=6 is recommended due to complexity): "))
print("Number of Hamiltonian paths:", hamiltonian_paths_with_symmetry(n))
