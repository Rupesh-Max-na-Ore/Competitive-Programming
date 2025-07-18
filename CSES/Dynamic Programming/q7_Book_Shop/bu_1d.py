n, x = map(int, input().split())
prices = list(map(int, input().split()))
pages = list(map(int, input().split()))

dp = [0] * (x + 1)

for i in range(n):  # For each book
    price = prices[i]
    page = pages[i]
    # Traverse backwards to prevent using the same book more than once
    for j in range(x, price - 1, -1):
        dp[j] = max(dp[j], dp[j - price] + page)

print(dp[x])
