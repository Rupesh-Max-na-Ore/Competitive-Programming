#include<bits/stdc++.h>
#define int long long int
#define F first
#define S second
#define pb push_back
#define RIGHT 0
#define LEFT 1
#define DOWN 2
#define UP 3
#define isValid(a,b,c) (a>=b && a < c ? 1: 0)
using namespace std;
int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};
string str;
int vis[7][7];
void solve()
{

}
int countPaths(int x,int y, int pos)
{
	if(pos == (int)str.length())
		return (x==6 && y==0);
	if(x == 6 && y == 0)
		return 0;
	if(vis[x][y])
		return 0;
	vector<bool> visited(4,-1);
	for(int k = 0; k < 4; k++)
	{
		if(isValid(x + dx[k],0,7) && isValid(y + dy[k],0,7))
			visited[k] = vis[x + dx[k]][y+dy[k]];
	}
	if(!visited[DOWN] && !visited[UP] && visited[RIGHT] && visited[LEFT])
		return 0;
	if(!visited[RIGHT] && !visited[LEFT] && visited[DOWN] && visited[UP])
		return 0;
	if(isValid(x-1,0,7) && isValid(y+1,0,7) && vis[x-1][y+1]==1)
	{
		if(!visited[RIGHT] && !visited[UP])
		   return 0;
	}
	if(isValid(x+1,0,7) && isValid(y+1,0,7) && vis[x+1][y+1]==1)
	{
		if(!visited[RIGHT] && !visited[DOWN])
		   return 0;
	}
	if(isValid(x-1,0,7) && isValid(y-1,0,7) && vis[x-1][y-1]==1)
	{
		if(!visited[LEFT] && !visited[UP])
		   return 0;
	}
	if(isValid(x+1,0,7) && isValid(y-1,0,7) && vis[x+1][y-1]==1)
	{
		if(!visited[LEFT] && !visited[DOWN])
		   return 0;
	}
	vis[x][y] = 1;
	int numOfPaths = 0; 
	if(str[pos] == '?')
	{
		for(int k = 0; k < 4; k++)
		{
			if(isValid(x+dx[k],0,7) && isValid(y+dy[k],0,7))
				numOfPaths += countPaths(x+dx[k], y+dy[k], pos+1);
		}
	}
	else if(str[pos] == 'R' && y + 1 < 7)
		numOfPaths+= countPaths(x,y+1,pos+1);
	else if(str[pos] == 'L' && y -1 >= 0)
		numOfPaths+= countPaths(x,y-1,pos+1);
	else if(str[pos] == 'U' && x -1 >= 0)
		numOfPaths+= countPaths(x-1,y,pos+1);
	else if(str[pos] == 'D' && x + 1 < 7)
		numOfPaths+= countPaths(x+1,y,pos+1);
	vis[x][y] = 0;
	return numOfPaths;

}
int32_t main()
{
    #ifndef ONLINE_JUDGE
       freopen("input.txt","r",stdin);
       freopen("output.txt","w",stdout);
    #endif
       cin >> str;
       cout << countPaths(0,0,0) << endl;
       
       
}