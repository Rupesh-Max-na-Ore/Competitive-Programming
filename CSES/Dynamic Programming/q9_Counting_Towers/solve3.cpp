#include<bits/stdc++.h>

#define MOD 1000000007
 
using namespace std;

vector<vector<int>> dp(1e6 + 1, vector<int>(2));
int main(){
    dp[0][0] = 1;
    dp[0][1] = 1;

    
    for(int i = 1; i < 1e6; i++){
        dp[i][0] = (2LL * dp[i-1][0] + dp[i-1][1]) % MOD;
        dp[i][1] = (4LL * dp[i-1][1] + dp[i-1][0]) % MOD;
    }
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        cout << (dp[n-1][0] + dp[n-1][1]) % MOD << endl;
    }

}