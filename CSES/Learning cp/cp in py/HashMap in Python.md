In Python, a **hashmap** is implemented using the built-in data structure called a **dictionary** (`dict`). Here's a step-by-step guide on how to create a hashmap, insert elements, and print them:

---

### ✅ 1. **Create a Hashmap**

```python
hashmap = {}
```

---

### ✅ 2. **Insert Elements**

You can insert (key, value) pairs like this:

```python
hashmap["apple"] = 5
hashmap["banana"] = 3
hashmap["orange"] = 8
```

---

### ✅ 3. **Print the Entire Hashmap**

```python
print(hashmap)
```

Output:

```python
{'apple': 5, 'banana': 3, 'orange': 8}
```

---

### ✅ 4. **Print All Keys and Values Separately**

```python
for key in hashmap:
    print(f"Key: {key}, Value: {hashmap[key]}")
```

or using `.items()`:

```python
for key, value in hashmap.items():
    print(f"{key} -> {value}")
```

---

### ✅ 5. **Example: Count Frequency of Words**

```python
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Print frequencies
for word, count in frequency.items():
    print(f"{word}: {count}")
```

Output:

```
apple: 3
banana: 2
orange: 1
```

---

Let me know if you want to use `defaultdict` or `Counter` from `collections` for easier frequency counting or other tricks with hashmaps!

Great! Python’s `collections` module provides **`defaultdict`** and **`Counter`**, which are powerful and efficient tools for working with hashmaps—especially for counting and grouping. Let’s go through both with clear examples.

---

## ✅ 1. `defaultdict` – Automatically Handles Missing Keys

### 🔹 Use case:

You don’t want to manually check if a key exists before updating it.

### 🔹 How it works:

You provide a default **value type** (like `int`, `list`, etc.) that will be used for missing keys.

### 🔹 Example 1: Counting frequencies

```python
from collections import defaultdict

frequency = defaultdict(int)

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
for word in words:
    frequency[word] += 1

for word, count in frequency.items():
    print(f"{word}: {count}")
```

> This is the same as using a normal `dict` with a manual check, but much cleaner.

---

### 🔹 Example 2: Grouping values

```python
from collections import defaultdict

grouped = defaultdict(list)
pairs = [(1, "a"), (2, "b"), (1, "c"), (2, "d")]

for key, value in pairs:
    grouped[key].append(value)

for key, values in grouped.items():
    print(f"{key} -> {values}")
```

Output:

```
1 -> ['a', 'c']
2 -> ['b', 'd']
```

---

## ✅ 2. `Counter` – For Counting Elements in One Line

### 🔹 Use case:

You want to quickly count how many times each item appears in a list, string, etc.

### 🔹 How it works:

Pass an iterable (like a list or string) and it returns a dictionary-like object.

### 🔹 Example 1: Count words

```python
from collections import Counter

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = Counter(words)

print(count)
```

Output:

```
Counter({'apple': 3, 'banana': 2, 'orange': 1})
```

---

### 🔹 Example 2: Most common elements

```python
print(count.most_common(2))  # Top 2 most common words
```

Output:

```
[('apple', 3), ('banana', 2)]
```

---

### 🔹 Example 3: Count characters in a string

```python
text = "hello world"
char_count = Counter(text)
print(char_count)
```

---

## 🔁 Summary

| Tool          | Best For                      | Auto Default | Example                    |
| ------------- | ----------------------------- | ------------ | -------------------------- |
| `dict`        | General key-value storage     | ❌            | `mydict['a'] = 1`          |
| `defaultdict` | Grouping or auto-initializing | ✅            | `defaultdict(int or list)` |
| `Counter`     | Counting items in an iterable | ✅            | `Counter(list or string)`  |

Let me know if you want a cheat sheet or small visual diagram to remember the differences!
