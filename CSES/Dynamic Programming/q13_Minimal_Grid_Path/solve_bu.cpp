#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<vector<char>> grid(n, vector<char>(n));
    vector<vector<string>> dp(n, vector<string>(n));

    for (int i = 0; i < n; ++i) {
        string row;
        cin >> row;
        for (int j = 0; j < n; ++j) {
            grid[i][j] = row[j];
        }
    }

    // fill from bottom-right to top-left
    for (int i = n - 1; i >= 0; --i) {
        for (int j = n - 1; j >= 0; --j) {
            if (i == n - 1 && j == n - 1) {
                dp[i][j] = string(1, grid[i][j]);
            } else {
                string down = (i + 1 < n) ? dp[i + 1][j] : "~";
                string right = (j + 1 < n) ? dp[i][j + 1] : "~";
                dp[i][j] = grid[i][j] + min(down, right);
            }
        }
    }

    cout << dp[0][0] << endl;
    return 0;
}
