def gcolor(n, m, grid):
    from random import shuffle

    result = [['' for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            neighbors = set()

            # check up, down, left, right neighbors in result (already processed)
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m and result[ni][nj] != '':
                    neighbors.add(result[ni][nj])

            # choose a color different from original and from neighbors
            for c in "ABCD":
                if c != grid[i][j] and c not in neighbors:
                    result[i][j] = c
                    break
            else:
                print("IMPOSSIBLE")
                return

    for row in result:
        print("".join(row))

# Input handling
n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

gcolor(n, m, grid)