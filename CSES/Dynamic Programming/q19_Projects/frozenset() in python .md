We dig into **`frozenset`** in Python.

---

## **What is a frozenset?**

* `frozenset` is the **immutable** version of a `set`.
* It contains **unique, unordered, hashable elements**, just like a normal set.
* Unlike a normal set, it **cannot be modified** after creation — no `.add()` or `.remove()`.
* Because it’s immutable, it’s **hashable** → can be used as a **dictionary key** or stored in another set.
* Syntax:

  ```python
  fs = frozenset([1, 2, 3])
  ```

---

## **Why is this relevant for memoization?**

Python’s `functools.lru_cache` and dict-based memoization require the state key to be **hashable**.

* Normal `set` → ❌ not hashable.
* `frozenset` → ✅ hashable.

Example:

```python
from functools import lru_cache

@lru_cache(None)
def f(s):
    print("Computing for", s)
    return sum(s)

print(f(frozenset([1, 2, 3])))
print(f(frozenset([1, 2, 3])))  # Cached
```

Output:

```
Computing for frozenset({1, 2, 3})
6
6
```

---

## **Key differences from set**

| Feature                                  | `set` | `frozenset` |
| ---------------------------------------- | ----- | ----------- |
| Mutable                                  | ✅     | ❌           |
| Hashable (usable as dict key)            | ❌     | ✅           |
| Supports `.add()` / `.remove()`          | ✅     | ❌           |
| Supports union, intersection, difference | ✅     | ✅           |
| Order guaranteed?                        | ❌     | ❌           |

---

## **Common operations**

```python
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

print(fs1 | fs2)   # Union -> frozenset({1, 2, 3, 4, 5})
print(fs1 & fs2)   # Intersection -> frozenset({3})
print(fs1 - fs2)   # Difference -> frozenset({1, 2})

# Convert back to set (mutable)
s = set(fs1)
```

---

## **In our backtracking problem**

When we do:

```python
@lru_cache(None)
def fn(i, booked_frozenset):
    booked = set(booked_frozenset)  # mutable copy for checks
    ...
    new_booked = booked.union(to_chk)
    return fn(i + 1, frozenset(new_booked))
```

We’re **freezing** the state before storing it in the cache,
but still making a mutable copy inside so we can operate normally.

---
