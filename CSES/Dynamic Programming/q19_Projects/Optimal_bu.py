import bisect
import sys

input = sys.stdin.read
data = input().split()
# Remember to do manual ctrl+d after pasting I/P when manual testing
# In CSES stdin closes automatically after TC i/p
n = int(data[0])

projects = []
idx = 1
for _ in range(n):
    a = int(data[idx])
    b = int(data[idx + 1])
    p = int(data[idx + 2])
    idx += 3
    projects.append((a, b, p))

# Sort by start time
projects.sort(key=lambda x: x[0])
starts = [a for a, _, _ in projects]

# Precompute next index
next_idx = []
for i in range(n):
    _, b, _ = projects[i]
    j = bisect.bisect_right(starts, b)
    next_idx.append(j)

# DP array
dp = [0] * (n + 1)  # dp[n] = 0 base case
for i in range(n - 1, -1, -1):
    take = projects[i][2] + dp[next_idx[i]]
    skip = dp[i + 1]
    dp[i] = max(take, skip)

print(dp[0])
