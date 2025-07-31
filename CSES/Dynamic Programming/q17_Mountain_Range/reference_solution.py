def solve():
    n = int(input())
    v = list(map(int, input().split()))

    # Initialize nearest greater on the left and right
    l = [-1] * n  # index of nearest greater to the left
    r = [-1] * n  # index of nearest greater to the right

    # Pair each value with its index, and sort by height descending
    p = sorted([(v[i], i) for i in range(n)], reverse=True)

    # Find nearest greater element to the left using a monotonic stack
    stack = []
    for i in range(n):
        while stack and v[stack[-1]] <= v[i]:
            stack.pop()
        if stack:
            l[i] = stack[-1]
        stack.append(i)

    # Clear the stack for reuse
    stack.clear()

    # Find nearest greater element to the right using a monotonic stack
    for i in range(n - 1, -1, -1):
        while stack and v[stack[-1]] <= v[i]:
            stack.pop()
        if stack:
            r[i] = stack[-1]
        stack.append(i)

    # Initialize DP table: dp[i] = max number of mountains starting from i
    dp = [1] * n

    # Iterate over the mountains from tallest to shortest
    for height, idx in p:
        if r[idx] != -1:
            dp[idx] = max(dp[idx], dp[r[idx]] + 1)
        if l[idx] != -1:
            dp[idx] = max(dp[idx], dp[l[idx]] + 1)

    # The answer is the maximum DP value
    print(max(dp))


# Run the function
solve()
