To **convert a hash set to a list** in Python, simply use the built-in `list()` constructor:

---

### ✅ **Syntax**

```python
my_set = {1, 2, 3}
my_list = list(my_set)
```

---

### 🔍 **Details**

* The resulting list will contain all elements of the set.
* The **order** of elements in the list is **not guaranteed**, since sets are **unordered**.
* If you want the list in a particular order, use `sorted()` or `list(sorted(...))`.

---

### 📌 **Examples**

#### 1. Convert set to list:

```python
s = {5, 2, 9}
l = list(s)
print(l)  # e.g., [2, 5, 9] or any permutation
```

#### 2. Convert and sort:

```python
sorted_list = sorted(s)
print(sorted_list)  # [2, 5, 9]
```

#### 3. Convert while preserving insertion order (Python 3.7+ preserves insertion order in sets):

```python
s = {1, 2, 3}
l = list(s)
print(l)  # [1, 2, 3]
```

---

### ⏱️ **Time Complexity**

* Converting a set of size $n$ to a list: **O(n)**
* Sorting the list (if needed): **O(n \log n)**

---

Let me know if you want to convert a **nested set** (e.g., set of tuples) or apply a transformation while converting.
