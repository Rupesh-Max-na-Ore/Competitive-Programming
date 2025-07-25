In Python, **strings are immutable**, so you can’t directly append characters to them like you would with a list. But you can **build a new string** by **concatenating** characters.

### ✅ Best Practice: Use a List and Join Later

This is the most efficient method, especially in loops:

```python
chars = []
chars.append('a')
chars.append('b')
chars.append('c')

result = ''.join(chars)
print(result)  # Output: 'abc'
```

### ❌ Inefficient Method: Direct Concatenation (OK for small cases)

```python
s = ""
s += 'a'
s += 'b'
s += 'c'
print(s)  # Output: 'abc'
```

> This works but is slower in loops because a new string is created each time.

---

### Summary

| Method                            | Use When                                       |
| --------------------------------- | ---------------------------------------------- |
| `s += 'x'`                        | One-off or short strings                       |
| `list.append()` + `''.join(list)` | Repeated appending in loops — best performance |

Let me know if you're working with a huge string or need help optimizing it.
