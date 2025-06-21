To find the **number of digits** in a number in Python, here are the most common ways:

---

### ✅ Method 1: Using `len(str(abs(n)))`

```python
n = 12345
num_digits = len(str(abs(n)))
print(num_digits)  # Output: 5
```

* `str(n)` converts the number to string.
* `abs(n)` handles negative numbers.
* `len(...)` counts the digits.

---

### ✅ Method 2: Using `math.log10()` (Only for **positive** numbers)

```python
import math

n = 12345
num_digits = math.floor(math.log10(n)) + 1
print(num_digits)  # Output: 5
```

* Fast, but doesn't work for `n = 0` or negative numbers unless handled explicitly.

---

### ✅ Method 3: Manual loop (For learning)

```python
n = 12345
count = 0
while n:
    n //= 10
    count += 1
print(count)  # Output: 5
```

* Good for understanding logic.
* Make sure `n ≠ 0`, else it gives 0.

---

### ✅ Special Case: When `n == 0`

```python
n = 0
num_digits = 1 if n == 0 else len(str(abs(n)))
print(num_digits)  # Output: 1
```

---

Would you like a function version of this for reuse?
