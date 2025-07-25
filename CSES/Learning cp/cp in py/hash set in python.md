In Python, a **hash set** is implemented using the built-in `set` type. A `set` is an **unordered collection** of **unique**, **hashable** elements. Internally, it is implemented as a **hash table**, giving average-case **O(1)** time complexity for insertion, deletion, and membership tests.

---

### ✅ **Formal Definition**

Let $S \subseteq U$ be a set, where $U$ is a universe of hashable objects. Then:

* $\texttt{set} : \mathcal{P}(U)$
* $\forall x \in S, y \in S : x = y \Rightarrow x \equiv y$
* $x \in S \Rightarrow \texttt{hash}(x) = h(x)$, with $h: U \to \mathbb{Z}$

The hash set maintains:

* **Uniqueness:** No duplicates.
* **Hashability:** Elements must be immutable and implement `__hash__()` and `__eq__()`.

---

### 🧪 **Basic Usage**

```python
# Creating a hash set
s = set()

# Insertion (O(1) average case)
s.add(10)
s.add(20)
s.add(10)  # Duplicate, will not be added

# Membership test (O(1) average case)
print(10 in s)   # True
print(30 in s)   # False

# Deletion (O(1) average case)
s.remove(20)     # Raises KeyError if not present
s.discard(30)    # No error if not present

# Iteration (O(n))
for elem in s:
    print(elem)
```

---

### ⚙️ **Hash Function Behavior**

* `set` relies on the hash function $h(x)$ to store and lookup elements.
* Only **immutable** and **hashable** objects can be added to a set:

  * ✅ `int`, `str`, `tuple` (if all elements are hashable)
  * ❌ `list`, `dict`, `set` (mutable and unhashable)

```python
hash(42)        # valid
hash("abc")     # valid
hash((1, 2))    # valid
hash([1, 2])    # TypeError
```

---

### ⏱️ **Time Complexities (Average Case)**

| Operation   | Time Complexity |
| ----------- | --------------- |
| `add(x)`    | O(1)            |
| `remove(x)` | O(1)            |
| `x in s`    | O(1)            |
| `len(s)`    | O(1)            |
| Iteration   | O(n)            |

> Worst-case lookup may degrade to O(n) due to hash collisions, but with a good hash function and internal resizing, this is rare.

---

### 🧠 **Mathematical Analogy**

Let:

* $h: U \rightarrow [0, m-1]$ be a hash function
* $T[0 \ldots m-1]$ be a table storing sets of keys (usually handled by open addressing or chaining internally)

Then set membership query is conceptually:

$$
\text{lookup}(x) = x \in T[h(x)]
$$

---

### 🔁 **Set Operations**

Python sets support standard set operations:

```python
A = {1, 2, 3}
B = {3, 4, 5}

A.union(B)        # {1, 2, 3, 4, 5}
A.intersection(B) # {3}
A.difference(B)   # {1, 2}
A.issubset(B)     # False
```

---

### 📌 Notes

* Python `frozenset` is an immutable version of `set`, and **hashable**, so it can be used as a dictionary key or added to a set.
* If you're using `set` in performance-critical applications or dealing with large datasets, understand the **underlying hash behavior** and consider the **load factor** and **resizing cost**.

---

If you want a **custom implementation** of a hash set or comparison with `dict`, or want to see how hash collisions are handled internally in CPython, I can provide those details too.



