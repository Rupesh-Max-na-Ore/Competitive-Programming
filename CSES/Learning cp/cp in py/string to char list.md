To turn a string into a list of characters in Python, you can use the built-in `list()` function:

```python
s = "HELLO"
char_list = list(s)
print(char_list)
```

### Output:

```
['H', 'E', 'L', 'L', 'O']
```

---

### Alternative (less common but instructive):

Using a list comprehension:

```python
char_list = [ch for ch in s]
```

Both methods give the same result: a list of characters from the string.
