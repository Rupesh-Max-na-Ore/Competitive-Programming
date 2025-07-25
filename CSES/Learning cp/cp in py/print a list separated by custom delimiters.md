# How to print a list separated by custom delimiters?

To **print a list separated by a custom delimiter** in Python, use the `str.join()` method.

---

### ✅ **Syntax**

```python
print(delimiter.join(map(str, my_list)))
```

---

### 🧪 **Examples**

#### 1. Basic list with a comma:

```python
lst = [1, 2, 3, 4]
print(', '.join(map(str, lst)))
# Output: 1, 2, 3, 4
```

#### 2. Custom delimiter:

```python
print(' | '.join(map(str, lst)))
# Output: 1 | 2 | 3 | 4
```

#### 3. Newline separator:

```python
print('\n'.join(map(str, lst)))
# Output:
# 1
# 2
# 3
# 4
```

#### 4. Using f-strings for more complex formatting:

```python
print(' - '.join(f"[{x}]" for x in lst))
# Output: [1] - [2] - [3] - [4]
```

---

### 🔁 **Why `map(str, lst)`?**

* `str.join()` works on **iterables of strings only**.
* If the list contains non-string elements (e.g., `int`, `float`, etc.), you must convert them to `str`.

---

Let me know if you want delimiter-based printing for **nested lists**, **matrix-style**, or with **index annotations**.
