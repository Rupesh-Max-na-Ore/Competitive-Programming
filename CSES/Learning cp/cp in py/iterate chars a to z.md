To iterate over characters from `'a'` to `'z'` in Python, you can use the `chr()` and `ord()` functions, or more simply, use the `string` module.

---

### ✅ Method 1: Using `chr()` and `ord()`

```python
for c in range(ord('a'), ord('z') + 1):
    print(chr(c), end=' ')
```

* `ord('a')` gives ASCII value of `'a'` → 97
* `chr(97)` gives the character `'a'`

So this loops from 97 to 122 (inclusive), converting each to the corresponding letter.

---

### ✅ Method 2: Using `string.ascii_lowercase`

```python
import string

for c in string.ascii_lowercase:
    print(c, end=' ')
```

* `string.ascii_lowercase` is `'abcdefghijklmnopqrstuvwxyz'`

This is **cleanest and most readable**.

---

### Bonus: If you want **uppercase letters**, use:

```python
for c in string.ascii_uppercase:
    print(c, end=' ')
```

Let me know if you want to do something with each letter (e.g., mapping to index, forming keys, etc.)!
