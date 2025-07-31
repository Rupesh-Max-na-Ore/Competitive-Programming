 7 weeks ago, hide # |
  Vote: I like it +8 Vote: I do not like it

Here is my solution for the Mountain Range, it's a simple solution (no segment tree/fenwik tree/any new sorting techniques). just start from the highest mountain and run a dp such that i'th index is updated using the nearest higher mountain at left and right of it(if they exist).

#include <bits/stdc++.h>
using namespace std;
// typedef long long ll;
// #define int ll

void solve(int tc = 0) {
    int n;
    cin >> n;
    std::vector<int> v(n), l(n, -1), r(n, -1), ls(n, -1), rs(n, -1);
    std::vector<pair<int, int>> p(n);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
        p[i] = {v[i], i};
    }
    sort(p.rbegin(), p.rend());
 
    stack<int> st;
    for (int i = 0; i < n; i++) {
        while (!st.empty() && v[st.top()] <= v[i]) {
            st.pop();
        }
        if (!st.empty())  {
            l[i] = st.top();
        }
        st.push(i);
    }
 
    while (!st.empty()) {
        st.pop();
    }
 
    for (int i = n - 1; i >= 0; i--) {
        while (!st.empty() && v[st.top()] <= v[i]) {
            st.pop();
        }
        if (!st.empty())  {
            r[i] = st.top();
        }
        st.push(i);
    }


    vector<int> dp(n, 1);

    for (auto &[x, y] : p) {
        if (r[y] != -1) {
            dp[y] = max(dp[y], dp[r[y]] + 1);
        }
        if (l[y] != -1) {
            dp[y] = max(dp[y], dp[l[y]] + 1); 
        }
    }

    cout << *max_element(dp.begin(), dp.end());
 
 
}
 
int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
 
    int O_O = 1;
    // cin >> O_O;
    while (O_O--) {
        solve();
        cout << "\n";
    }
 
    return 0;
}

