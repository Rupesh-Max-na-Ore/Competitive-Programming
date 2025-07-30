You're currently using the **classic "optimal strategy for a game" recurrence** for the **Removal Game**:

---

## ✅ Problem Recap

Let $a[0..n-1]$ be the coin values.

Players pick either end, and both play **optimally**.
You are computing the **maximum score** the **first player** can get.

Your recurrence is:

```python
dp[l][r] = max(
    a[l] + min(dp[l + 2][r], dp[l + 1][r - 1]),
    a[r] + min(dp[l + 1][r - 1], dp[l][r - 2])
)
```

---

### ✅ Let's now convert it to a **bottom-up tabulation** approach.

---

## ✅ Step-by-Step Tabulation

1. We'll define `dp[l][r]` as: the **maximum score the current player can achieve** in the subarray $a[l \ldots r]$.
2. Initialize base cases:

   * `dp[i][i] = a[i]`  (only one coin)
   * `dp[i][i+1] = max(a[i], a[i+1])` (two coins)
3. Fill in increasing order of subarray length.

---

### ✅ Bottom-Up Code:

```python
n = int(input())
a = list(map(int, input().split()))
dp = [[0] * n for _ in range(n)]

# Base cases
for i in range(n):
    dp[i][i] = a[i]
for i in range(n - 1):
    dp[i][i + 1] = max(a[i], a[i + 1])

# Fill for lengths >= 3
for length in range(3, n + 1):  # length of subarray
    for l in range(n - length + 1):
        r = l + length - 1
        dp[l][r] = max(
            a[l] + min(dp[l + 2][r] if l + 2 <= r else 0, dp[l + 1][r - 1] if l + 1 <= r - 1 else 0),
            a[r] + min(dp[l + 1][r - 1] if l + 1 <= r - 1 else 0, dp[l][r - 2] if l <= r - 2 else 0)
        )

print(dp[0][n - 1])
```

---

### ✅ Notes:

* We use conditionals like `if l + 2 <= r else 0` to avoid index out-of-bound errors.
* This implementation avoids recursion and builds from small intervals to large ones.

---

### ✅ Time and Space Complexity

* Time: $O(n^2)$
* Space: $O(n^2)$

---

Let me know if you want a **space-optimized** version or **trace of moves** (i.e., what moves each player makes).
