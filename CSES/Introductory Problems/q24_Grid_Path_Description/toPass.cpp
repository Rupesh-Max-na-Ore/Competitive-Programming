#include <bits/stdc++.h>
#include <unordered_map>
#include <time.h>
 
#define ll long long int
#define MOD 1000000007
using namespace std;
 
string s;
vector<ll> arr;
 
ll t, r, c, k, x, A, B, y, z, m, n;
 
bool isPalin(string& s) {
	for (int i = 0; i < s.size(); i++) {
		if (s[i] != s[s.size() - 1 - i]) {
			return false;
		}
	}
	return true;
}
 
bool isIncr(vector<ll>& a) {
	for (int i = 0; i < a.size() - 1; i++) {
		if (a[i] > a[i + 1]) {
			return false;
		}
	}
	return true;
}
 
vector<pair<int, int>> adj = { {0, 1}, {1, 0} , {0, -1}, {-1, 0} };
 
bool inBounds(int i, int j, int n, int m) {
	return (i >= 0 && i < n&& j >= 0 && j < m);
}
 
 
ll fact(ll n) {
	if (n == 0 || n == 1)
		return 1;
	else
		return n * fact(n - 1);
}
 
ll power(ll x, ll y, ll m) {
	if (y == 0)
		return 1;
	ll p = power(x, y / 2, m) % m;
	p = (p * p) % m;
 
	return (y % 2 == 0) ? p : (x * p) % m;
}
 
 
int gcd(int a, int b) {
	if (a == 0)
		return b;
	return gcd(b % a, a);
 
}
ll modInverse(ll a, ll m)
{
	ll g = gcd(a, m);
	if (g != 1)return -1;
	else
	{
		return power(a, m - 2, m);
	}
}
 
void print(vector<ll>& arr) {
	for (auto x : arr) {
		cout << x << " ";
	}
	cout << endl;
}
 
double euclid(pair<int, int>& f, pair<int, int>& s) {
	return sqrt((f.second - s.second) * (f.second - s.second) + (f.first - s.first) * (f.first - s.first));
}
 
ll sum(ll n) {
 
	ll inverse = modInverse(2, MOD);
	n = ((n % MOD) * ((n + 1) % MOD)) % MOD;
	n *= inverse;
	return n % MOD;
}
 
int numDigits(int result) {
	int ans = 0;
 
	while (result > 0) {
		ans++;
		result /= 10;
	}
	return ans;
}
 
bool visited[7][7];
int paths = 0, steps = 0;
int reserved[49];
 
void solved(int r, int c) {
 
	if (r == 6 && c == 0) {
		if (steps == 48) {
			paths++;
		}
		return;
	}
 
	if (visited[r][c] || (
		
		
			((c >= 1 && c <= 5 && !visited[r][c + 1] && !visited[r][c - 1]) &&
			((r == 0 && visited[r + 1][c]) || (r == 6 && visited[r - 1][c]))) 
		||
			((r >= 1 && r <= 5 && !visited[r + 1][c] && !visited[r - 1][c]) &&
				((c == 0 && visited[r][c + 1]) || (c == 6 && visited[r][c - 1]))) 
		
		|| (r >= 1 && r <= 5 && c >= 1 && c <= 5 && visited[r + 1][c] 
			&& visited[r - 1][c] && !visited[r][c + 1] && !visited[r][c - 1])
 
		|| (r >= 1 && r <= 5 && c >= 1 && c <= 5 && visited[r][c + 1] && visited[r][c - 1] 
			&& !visited[r + 1][c] && !visited[r - 1][c])))
	{
		return;
	}
 
	visited[r][c] = true;
 
	if (reserved[steps] != -1) {
 
		switch (reserved[steps]) {
		case 0:
			if (r > 0 && !visited[r - 1][c]) {
				steps++;
				solved(r - 1, c); // up
				steps--;
			}
			break;
		case 1:
			if (r < 6 && !visited[r + 1][c]) {
				steps++;
				solved(r + 1, c);  //down
				steps--;
			}
			break;
		case 2:
			if (c > 0 && !visited[r][c - 1]) {
				steps++;
				solved(r, c - 1); //left
				steps--;
			}
			break;
		case 3:
			if (c < 6 && !visited[r][c + 1]) {
				steps++;
				solved(r, c + 1); // right
				steps--;
			}
			break;
 
		}
		
		visited[r][c] = false;
		return;
	}
 
	if (r < 6 && !visited[r + 1][c]) {
		steps++;
		solved(r + 1, c);  //down
		steps--;
	}
 
	if (r > 0 && !visited[r - 1][c]) {
		steps++;
		solved(r - 1, c); // up
		steps--;
	}
	
	if (c > 0 && !visited[r][c - 1]) {
		steps++;
		solved(r, c - 1); //left
		steps--;
	}
 
	if (c < 6 && !visited[r][c + 1]) {
		steps++;
		solved(r, c + 1); // right
		steps--;
	}
 
	visited[r][c] = false;
 
}
 
 
 
int main() {
 
	clock_t start = clock();
	ios_base::sync_with_stdio(false);
	
	cin >> s;
 
	for (int i = 0; i < s.size(); i++) {
		switch (s[i]) {
		case '?':
			reserved[i] = -1;
			break;
		case 'U':
			reserved[i] = 0;
			break;
		case 'D':
			reserved[i] = 1;
			break;
		case 'L':
			reserved[i] = 2;
			break;
		case 'R':
			reserved[i] = 3;
			break;
 
		}
	}
 
	solved(0, 0);
	cout << paths << endl;
	
	return 0;
}