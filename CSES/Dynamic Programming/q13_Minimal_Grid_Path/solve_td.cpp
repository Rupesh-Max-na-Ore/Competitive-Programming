#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int n;
vector<vector<char>> grid;
vector<vector<string>> memo;

string dfs(int i, int j) {
    if (i >= n || j >= n) return "~"; // large string to simulate infinity
    if (i == n - 1 && j == n - 1) return string(1, grid[i][j]);

    if (!memo[i][j].empty()) return memo[i][j];

    string down = dfs(i + 1, j);
    string right = dfs(i, j + 1);

    memo[i][j] = grid[i][j] + min(down, right);
    return memo[i][j];
}

int main() {
    cin >> n;
    grid.resize(n, vector<char>(n));
    memo.resize(n, vector<string>(n));

    for (int i = 0; i < n; ++i) {
        string row;
        cin >> row;
        for (int j = 0; j < n; ++j) {
            grid[i][j] = row[j];
        }
    }

    cout << dfs(0, 0) << endl;
    return 0;
}
