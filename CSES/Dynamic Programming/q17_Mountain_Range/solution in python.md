Here is the **Python translation** of your C++ code for the **Mountain Range** problem, preserving your algorithm's logic and adding **clear comments** throughout:

---

### ✅ Python Version (with comments)

```python
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
```

---

### 📌 Explanation

* You precompute the **nearest higher mountain** to the **left** and **right** of each mountain using **monotonic stacks**.
* Then, starting from the **tallest mountain**, you update the `dp[i]` value by checking the `dp` values of its adjacent higher mountains (left and right).
* The idea is that if you can glide to a smaller mountain from a higher one, the DP value of the smaller one depends on the longer paths from the higher one.

---

### 🔁 Differences from Original Recursive Idea

Your version improves over naive recursion by:

* Processing in decreasing order of height.
* Leveraging the nearest taller mountains as "entry points" for glide paths.
* Using **O(n)** stack passes + **O(n)** DP updates — very efficient.

---

Let me know if you'd like to include the actual **glide sequence** in output, or want to visualize it for debugging.
