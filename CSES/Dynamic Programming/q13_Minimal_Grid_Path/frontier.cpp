// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr);

//     int n;
//     cin >> n;
//     vector<string> grid(n);
//     for(int i=0;i<n;i++) cin >> grid[i];

//     vector<pair<int,int>> frontier;
//     frontier.emplace_back(0,0);
//     string ans;
//     ans.push_back(grid[0][0]);

//     int maxd = 2 * n - 2;
//     vector<vector<bool>> seen(n, vector<bool>(n, false));

//     for(int d = 1; d <= maxd; ++d){
//         char best = 'Z' + 1;
//         vector<pair<int,int>> candidates;

//         for(auto [i,j]: frontier){
//             if(i+1 < n) best = min(best, grid[i+1][j]);
//             if(j+1 < n) best = min(best, grid[i][j+1]);
//         }
//         for(auto [i,j]: frontier){
//             if(i+1 < n && grid[i+1][j] == best) candidates.emplace_back(i+1, j);
//             if(j+1 < n && grid[i][j+1] == best) candidates.emplace_back(i, j+1);
//         }
//         // deduplicate
//         frontier.clear();
//         for(auto &p : candidates){
//             auto &x = seen[p.first][p.second];
//             if(!x){
//                 x = true;
//                 frontier.push_back(p);
//             }
//         }
//         for(auto &p : frontier){
//             seen[p.first][p.second] = false;
//         }

//         ans.push_back(best);
//     }

//     cout << ans << "\n";
//     return 0;
// }


#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<string> grid(n);
    for(int i=0; i<n; i++) cin >> grid[i];

    vector<pair<int,int>> frontier;
    frontier.emplace_back(0, 0);
    string ans;
    ans.push_back(grid[0][0]);

    int maxd = 2 * n - 2;
    vector<vector<char>> seen(n, vector<char>(n, 0));  // Fixed: use char instead of bool

    for(int d = 1; d <= maxd; ++d){
        char best = 'Z' + 1;
        vector<pair<int,int>> candidates;

        for(auto [i,j] : frontier){
            if(i + 1 < n) best = min(best, grid[i+1][j]);
            if(j + 1 < n) best = min(best, grid[i][j+1]);
        }

        for(auto [i,j] : frontier){
            if(i + 1 < n && grid[i+1][j] == best) candidates.emplace_back(i+1, j);
            if(j + 1 < n && grid[i][j+1] == best) candidates.emplace_back(i, j+1);
        }

        frontier.clear();
        for(auto &p : candidates){
            auto &x = seen[p.first][p.second]; // now works
            if(!x){
                x = 1;
                frontier.push_back(p);
            }
        }

        for(auto &p : frontier){
            seen[p.first][p.second] = 0;
        }

        ans.push_back(best);
    }

    cout << ans << "\n";
    return 0;
}
