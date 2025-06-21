dx = [0, 0, 1, -1]  # RIGHT, LEFT, DOWN, UP
dy = [1, -1, 0, 0]

def is_valid(a, b, c):
    return b <= a < c

vis = [[0 for _ in range(7)] for _ in range(7)]

def count_paths(x, y, pos, s):
    if pos == len(s):
        return int(x == 6 and y == 0)
    if x == 6 and y == 0:
        return 0
    if vis[x][y] == 1:
        return 0

    visited = [False] * 4
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if is_valid(nx, 0, 7) and is_valid(ny, 0, 7):
            visited[k] = vis[nx][ny] == 1

    if not visited[2] and not visited[3] and visited[0] and visited[1]:
        return 0
    if not visited[0] and not visited[1] and visited[2] and visited[3]:
        return 0

    if is_valid(x-1, 0, 7) and is_valid(y+1, 0, 7) and vis[x-1][y+1] == 1:
        if not visited[0] and not visited[3]:
            return 0
    if is_valid(x+1, 0, 7) and is_valid(y+1, 0, 7) and vis[x+1][y+1] == 1:
        if not visited[0] and not visited[2]:
            return 0
    if is_valid(x-1, 0, 7) and is_valid(y-1, 0, 7) and vis[x-1][y-1] == 1:
        if not visited[1] and not visited[3]:
            return 0
    if is_valid(x+1, 0, 7) and is_valid(y-1, 0, 7) and vis[x+1][y-1] == 1:
        if not visited[1] and not visited[2]:
            return 0

    vis[x][y] = 1
    num_paths = 0

    if s[pos] == '?':
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if is_valid(nx, 0, 7) and is_valid(ny, 0, 7):
                num_paths += count_paths(nx, ny, pos + 1, s)
    else:
        ch = s[pos]
        if ch == 'R' and y + 1 < 7:
            num_paths += count_paths(x, y + 1, pos + 1, s)
        elif ch == 'L' and y - 1 >= 0:
            num_paths += count_paths(x, y - 1, pos + 1, s)
        elif ch == 'U' and x - 1 >= 0:
            num_paths += count_paths(x - 1, y, pos + 1, s)
        elif ch == 'D' and x + 1 < 7:
            num_paths += count_paths(x + 1, y, pos + 1, s)

    vis[x][y] = 0
    return num_paths

if __name__ == "__main__":
    s = input().strip()
    print(count_paths(0, 0, 0, s))
