To convert a **list of characters** into a **string** in Python, use the `join()` method:

---

### ✅ Example:

```python
char_list = ['H', 'e', 'l', 'l', 'o']
string = ''.join(char_list)
print(string)
```

#### Output:

```
Hello
```

---

### 🧠 How it works:

* `''.join(list)` joins all elements of the list into a string.
* `''` means no separator between characters (you can change it to `' '`, `'-'`, etc. if needed).

---

### 🔁 If list has non-characters:

Make sure all elements are **strings**, or convert them first:

```python
mixed_list = ['A', 'B', 1, 2]
string = ''.join(map(str, mixed_list))
print(string)  # Output: AB12
```

Let me know if you want the reverse too (string → list of chars).
