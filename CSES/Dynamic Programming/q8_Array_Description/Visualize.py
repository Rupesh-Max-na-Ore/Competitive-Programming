# Another way to do it, just require to think a little different.
# Final ans are same, but interim results computed are different for dp table
MOD = 10**9 + 7

n, m = map(int, input().split())
a = list(map(int, input().split()))

# Step 1: Initialize DP table
dp = [[0] * (m + 2) for _ in range(n)]

# Step 2: Base case
if a[0] == 0:
    for v in range(1, m + 1):
        dp[0][v] = 1
else:
    dp[0][a[0]] = 1

print("DP table after filling index 0:")
print(dp[0][1 : m + 1])
print("-" * 40)

# Step 3: Iteratively fill the table
for i in range(1, n):
    for v in range(1, m + 1):
        if a[i] == 0 or a[i] == v:
            dp[i][v] = (dp[i - 1][v - 1] + dp[i - 1][v] + dp[i - 1][v + 1]) % MOD

    # Debug print: show the DP row at position i
    print(f"DP table after filling index {i}:")
    print(dp[i][1 : m + 1])  # show only values from 1 to m
    print("-" * 40)

# Step 4: Final answer is sum over last row
if a[-1] == 0:
    ans = sum(dp[n - 1][1 : m + 1]) % MOD
else:
    ans = dp[n - 1][a[-1]] % MOD

print("Final Result:", ans)
