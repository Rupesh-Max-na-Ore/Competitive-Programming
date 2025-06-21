You're given a problem where you must fill an `n × n` grid such that:

> **Each cell contains the MEX (Minimum EXcluded value)** — the **smallest non-negative integer** not found **to the left in the same row** or **above in the same column**.

---

## ✅ Understanding the MEX Grid Rule:

For each cell `(i, j)` in the grid:

* Look at all cells **left** in the same row: `(i, 0)` to `(i, j−1)`
* Look at all cells **above** in the same column: `(0, j)` to `(i−1, j)`
* Assign the **smallest non-negative integer** that is **not present** in those cells

---

### ✅ Step-by-step Plan:

1. Initialize an `n × n` grid.
2. For each cell `(i, j)`:

   * Gather used values in the row up to `j−1` and column up to `i−1`.
   * Compute the MEX of this set.
   * Assign MEX to cell `(i, j)`.

---

### ✅ Python Code

```python
def solve(n):
    grid = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            used = set()

            # Elements to the left in the same row
            for k in range(j):
                used.add(grid[i][k])

            # Elements above in the same column
            for k in range(i):
                used.add(grid[k][j])

            # Find the MEX (smallest non-negative integer not in 'used')
            mex = 0
            while mex in used:
                mex += 1

            grid[i][j] = mex

    # Print the grid
    for row in grid:
        print(" ".join(map(str, row)))

# Input
n = int(input())
solve(n)
```

---

### ✅ Sample Output for `n = 5`:

```
0 1 2 3 4
1 0 3 2 5
2 3 0 1 6
3 2 1 0 7
4 5 6 7 0
```

---

### ⏱️ Time Complexity:

* For each cell `(i, j)`, it checks up to `O(n)` items (row + column).
* Total: `O(n^3)` which is **fine for n ≤ 100**.

If you'd like a faster version using a more efficient MEX approach (like with frequency counters), I can also provide that.
