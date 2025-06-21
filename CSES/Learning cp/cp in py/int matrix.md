To initialize a **2D integer matrix of size `n × m` filled with zeroes** in Python, use a list comprehension:

### ✅ Method: List Comprehension

```python
n = 3  # number of rows
m = 4  # number of columns

matrix = [[0 for _ in range(m)] for _ in range(n)]
```

This creates a new list for each row, avoiding reference issues.

### 🧠 Why not `[[0]*m]*n`?

```python
matrix = [[0]*m]*n  # ❌ BAD for mutable objects
```

This creates **n references to the same row**, so changing one element will affect all rows. Example:

```python
matrix[0][0] = 1
print(matrix)
# All rows will show 1 at index [0] — undesired!
```

---

### 🧪 Example Output:

```python
for row in matrix:
    print(row)
```

```
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
```

Let me know if you want a version filled with something other than `0`.
