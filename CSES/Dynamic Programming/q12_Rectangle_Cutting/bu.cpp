#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    // dp[i][j] = minimum number of cuts for i x j rectangle
    vector<vector<int>> dp(a + 1, vector<int>(b + 1, 0));

    for (int i = 1; i <= a; ++i) {
        for (int j = 1; j <= b; ++j) {
            if (i == j) {
                dp[i][j] = 0; // already a square
            } else {
                int minCuts = INT_MAX;

                // vertical cuts (cut along height)
                for (int k = 1; k < i; ++k) {
                    minCuts = min(minCuts, 1 + dp[k][j] + dp[i - k][j]);
                }

                // horizontal cuts (cut along width)
                for (int k = 1; k < j; ++k) {
                    minCuts = min(minCuts, 1 + dp[i][k] + dp[i][j - k]);
                }

                dp[i][j] = minCuts;
            }
        }
    }

    cout << dp[a][b] << endl;
    return 0;
}
