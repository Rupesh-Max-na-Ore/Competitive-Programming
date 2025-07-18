n, x = map(int, input().split())
prices = list(map(int, input().split()))
pages = list(map(int, input().split()))

prev = [0] * (x + 1)
curr = [0] * (x + 1)

for i in range(n):
    price = prices[i]
    page = pages[i]
    for j in range(x + 1):
        # Do not take the item
        curr[j] = prev[j]
        # Try taking the item if we have enough budget
        if j >= price:
            curr[j] = max(curr[j], prev[j - price] + page)
    # Copy curr into prev for next iteration
    prev, curr = curr, prev  # Swap references to reuse arrays

print(prev[x])
