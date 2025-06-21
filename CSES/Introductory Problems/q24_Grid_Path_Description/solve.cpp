#include <iostream>
#include <string>
using namespace std;

const int N = 7;
bool visited[N][N];
string path;
int count = 0;

// Directions: U, D, L, R
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
char dir[4] = {'U', 'D', 'L', 'R'};

bool inBounds(int x, int y) {
    return x >= 0 && x < N && y >= 0 && y < N;
}

bool isTrapped(int x, int y) {
    // Check for horizontal wall and unvisited vertical neighbors
    if (x > 0 && x < N - 1 && !visited[x - 1][y] && !visited[x + 1][y]) {
        if (y == 0 || y == N - 1 || (visited[x][y - 1] && visited[x][y + 1]))
            return true;
    }

    // Check for vertical wall and unvisited horizontal neighbors
    if (y > 0 && y < N - 1 && !visited[x][y - 1] && !visited[x][y + 1]) {
        if (x == 0 || x == N - 1 || (visited[x - 1][y] && visited[x + 1][y]))
            return true;
    }

    return false;
}

void dfs(int x, int y, int step) {
    if (x == 6 && y == 0) {
        if (step == 48)
            count++;
        return;
    }

    if (step >= 48 || isTrapped(x, y))
        return;

    char move = path[step];
    for (int i = 0; i < 4; i++) {
        if (move != '?' && move != dir[i])
            continue;

        int nx = x + dx[i];
        int ny = y + dy[i];

        if (inBounds(nx, ny) && !visited[nx][ny]) {
            visited[nx][ny] = true;
            dfs(nx, ny, step + 1);
            visited[nx][ny] = false;
        }
    }
}

int main() {
    cin >> path;
    visited[0][0] = true;
    dfs(0, 0, 0);
    cout << count << endl;
    return 0;
}
