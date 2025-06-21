from collections import deque

def gcolor(n, m, grid):
    color = [['' for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    q = deque()
    q.append((0, 0))
    
    directions = [(0,1), (1,0), (0,-1), (-1,0)]  # Right, Down, Left, Up
    
    while q:
        x, y = q.popleft()
        
        if visited[y][x]:
            continue
        
        # Step 1: Gather used colors in neighbors
        neighbor_colors = set()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if color[ny][nx]:  # if already colored
                    neighbor_colors.add(color[ny][nx])
        
        # Step 2: Choose a valid color
        for c in 'ABCD':
            if c != grid[y][x] and c not in neighbor_colors:
                color[y][x] = c
                break
        else:
            print("IMPOSSIBLE")
            return
        
        visited[y][x] = True
        
        # Step 3: Enqueue unvisited neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
                q.append((nx, ny))
    
    # Output
    for row in color:
        print("".join(row))

# Input handling
n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
gcolor(n, m, grid)
