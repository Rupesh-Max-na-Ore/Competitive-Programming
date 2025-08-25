Good question 👍.
In Python, **bitwise operations** work directly on the **binary representation** of integers. These are very useful for problems like **subsets, masks, dynamic programming on subsets, CSES Elevator Rides, etc.**

---

## 📌 Bitwise Operators in Python

| Operator | Meaning                | Example  | Binary Example                  |     |     |             |             |
| -------- | ---------------------- | -------- | ------------------------------- | --- | --- | ----------- | ----------- |
| `&`      | AND                    | `a & b`  | `6 & 3 = 2` → `110 & 011 = 010` |     |     |             |             |
| \`       | \`                     | OR       | \`a                             | b\` | \`6 | 3 = 7`→`110 | 011 = 111\` |
| `^`      | XOR                    | `a ^ b`  | `6 ^ 3 = 5` → `110 ^ 011 = 101` |     |     |             |             |
| `~`      | NOT (bitwise negation) | `~a`     | `~6 = -7` (in 2’s complement)   |     |     |             |             |
| `<<`     | Left Shift             | `a << n` | `3 << 2 = 12` → `011 → 1100`    |     |     |             |             |
| `>>`     | Right Shift            | `a >> n` | `12 >> 2 = 3` → `1100 → 0011`   |     |     |             |             |

---

## 📌 Example Code

```python
a = 6   # 110 in binary
b = 3   # 011 in binary

print("a & b =", a & b)   # 2 (010)
print("a | b =", a | b)   # 7 (111)
print("a ^ b =", a ^ b)   # 5 (101)
print("~a =", ~a)         # -7
print("a << 1 =", a << 1) # 12 (1100)
print("a >> 1 =", a >> 1) # 3 (011)
```

---

## 📌 Common Use in Algorithms (Subsets)

Bitmasks are great for representing subsets.
If `n = 3`, then subsets are numbers `0` to `(1 << n) - 1` i.e., `0..7`.

```python
n = 3
for mask in range(1 << n):  # 0 to 7
    subset = []
    for i in range(n):
        if mask & (1 << i):  # check if i-th bit is set
            subset.append(i)
    print(mask, "->", subset)
```

**Output:**

```
0 -> []
1 -> [0]
2 -> [1]
3 -> [0, 1]
4 -> [2]
5 -> [0, 2]
6 -> [1, 2]
7 -> [0, 1, 2]
```

---

👉 Do you want me to **explain bitwise usage specifically in the Elevator Rides DP solution** (where we use masks to represent people in rides), or just keep it at this **general tutorial level**?
