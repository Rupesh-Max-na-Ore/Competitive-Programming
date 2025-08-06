#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    // Fast IO
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // Read input size
    int n;
    cin >> n;

    // Read array
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    // dp[i][par] where par = 0 means no previous element (like -1), par = 1 to n for actual indices
    vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0)); // dp[i][par]

    for (int i = n - 1; i >= 0; --i) {
        for (int par = 0; par <= i; ++par) {
            int pick = 0;
            int notPick = dp[i + 1][par];

            if (par == 0 || arr[i] > arr[par - 1]) {
                pick = 1 + dp[i + 1][i + 1]; // i+1 to simulate 1-based previous
            }

            dp[i][par] = max(pick, notPick);
        }
    }

    // Output result
    cout << dp[0][0] << '\n';

    return 0;
}
