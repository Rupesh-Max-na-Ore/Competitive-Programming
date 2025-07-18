def knapsack(i, budget, prices, pages, n):
    # Base case: no items left or no budget
    if i == n or budget == 0:
        return 0

    # Case 1: Exclude current book
    exclude = knapsack(i + 1, budget, prices, pages, n)

    # Case 2: Include current book (only if affordable)
    include = 0
    if prices[i] <= budget:
        include = pages[i] + knapsack(i + 1, budget - prices[i], prices, pages, n)

    return max(include, exclude)


# Input
n, x = map(int, input().split())
prices = list(map(int, input().split()))
pages = list(map(int, input().split()))

# Output
print(knapsack(0, x, prices, pages, n))
