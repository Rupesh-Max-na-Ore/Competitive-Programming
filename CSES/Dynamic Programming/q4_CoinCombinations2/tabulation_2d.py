def countWays(n, sum, curr):
    dp = [[0 for _ in range(sum+1)] for _ in range(n)]
    # i refers to coin indx, curr[i] is the ith coin in currency
    for i in range(n): 
        # 1 way to reach sum = 0 in any coin => excl it
        dp[i][0] = 1
    
    # Loop order can be reveresed for 2d tabulation, doesn't matter
    # cuz the prev col and row are avail to us at any point in time
    for s in range(1, sum+1):
        for i in range(n):
            incl = dp[i][s - curr[i]] if s >= curr[i] else 0
            excl = dp[i-1][s] if i > 0 else 0
            dp[i][s] = incl + excl
        # print(f"s == {s}")
        print (f"i == {i}")
        for row in dp:
            print(row)
    
    return dp[n-1][sum] 

n, sum = map(int, input().split())
curr = list(map(int, input().split()))
print(countWays(n, sum, curr))

"""
Reversed Loop Order - Column(Sum) wise update
for i in range(n):
        for s in range(1, sum+1):
3 9
2 3 5
s == 1
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
s == 2
[1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
[1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
[1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
s == 3
[1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
[1, 0, 1, 1, 0, 0, 0, 0, 0, 0]
[1, 0, 1, 1, 0, 0, 0, 0, 0, 0]
s == 4
[1, 0, 1, 0, 1, 0, 0, 0, 0, 0]
[1, 0, 1, 1, 1, 0, 0, 0, 0, 0]
[1, 0, 1, 1, 1, 0, 0, 0, 0, 0]
s == 5
[1, 0, 1, 0, 1, 0, 0, 0, 0, 0]
[1, 0, 1, 1, 1, 1, 0, 0, 0, 0]
[1, 0, 1, 1, 1, 2, 0, 0, 0, 0]
s == 6
[1, 0, 1, 0, 1, 0, 1, 0, 0, 0]
[1, 0, 1, 1, 1, 1, 2, 0, 0, 0]
[1, 0, 1, 1, 1, 2, 2, 0, 0, 0]
s == 7
[1, 0, 1, 0, 1, 0, 1, 0, 0, 0]
[1, 0, 1, 1, 1, 1, 2, 1, 0, 0]
[1, 0, 1, 1, 1, 2, 2, 2, 0, 0]
s == 8
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
[1, 0, 1, 1, 1, 1, 2, 1, 2, 0]
[1, 0, 1, 1, 1, 2, 2, 2, 3, 0]
s == 9
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
[1, 0, 1, 1, 1, 1, 2, 1, 2, 2]
[1, 0, 1, 1, 1, 2, 2, 2, 3, 3]

final:
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
[1, 0, 1, 1, 1, 1, 2, 1, 2, 2]
[1, 0, 1, 1, 1, 2, 2, 2, 3, 3]
3

vs 

Straight Loop Order - Row(Coin) wise update
for i in range(n):
        for s in range(1, sum+1):
3 9
2 3 5
i == 0
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i == 1
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
[1, 0, 1, 1, 1, 1, 2, 1, 2, 2]
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i == 2
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
[1, 0, 1, 1, 1, 1, 2, 1, 2, 2]
[1, 0, 1, 1, 1, 2, 2, 2, 3, 3]
3

"""