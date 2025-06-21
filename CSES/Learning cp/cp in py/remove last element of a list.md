You can remove the **last element** of a list in Python using any of the following:

---

### ✅ 1. `pop()` method (most common)

```python
my_list = [1, 2, 3, 4]
my_list.pop()  # removes 4
print(my_list)  # Output: [1, 2, 3]
```

> ⚠️ `pop()` **returns** the removed element and also **modifies** the original list.

---

### ✅ 2. Slicing (to create a new list without last element)

```python
my_list = [1, 2, 3, 4]
new_list = my_list[:-1]
print(new_list)  # Output: [1, 2, 3]
```

> ⚠️ This does **not modify** the original list.

---

### ✅ 3. `del` statement

```python
my_list = [1, 2, 3, 4]
del my_list[-1]
print(my_list)  # Output: [1, 2, 3]
```

---

Let me know if you want to remove multiple elements from the end or handle edge cases like empty lists.
