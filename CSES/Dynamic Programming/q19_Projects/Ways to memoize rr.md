rr.py
```python
n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

booked = set()

def fn(i, booked):
    if i == n:
        return 0

    # Option 1: skip this project
    excl = fn(i + 1, booked)

    # Option 2: include this project if no overlap
    start, end, reward = mat[i]
    to_chk = list(range(start, end + 1))
    for day in to_chk:
        if day in booked:
            return excl  # can't take it, overlap found

    # Book these days
    booked.update(to_chk)
    incl = reward + fn(i + 1, booked)
    # Backtrack (undo booking)
    booked.difference_update(to_chk)

    return max(excl, incl)

print(fn(0, booked))

```



We want to take this exact backtracking structure (same variables, same recursion shape) and **memoize** it so that we don’t recompute overlapping subproblems.

The challenge here:

* Your state is `(i, booked)`
* `booked` is a `set`, which is mutable & unhashable → cannot be directly used as a cache key.
* The naive backtracking marks individual days — but days can go up to $10^9$ — so we can’t store them directly in an efficient key for large inputs.

Still, if we memoize exactly, we have two main options:

---

## **1. Memoizing with `frozenset`**

We can freeze the booked set before storing it in the cache:

```python
from functools import lru_cache

n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

@lru_cache(None)
def fn(i, booked_frozenset):
    if i == n:
        return 0

    booked = set(booked_frozenset)

    # Option 1: skip this project
    excl = fn(i + 1, booked_frozenset)

    # Option 2: take this project if no overlap
    start, end, reward = mat[i]
    to_chk = range(start, end + 1)
    for day in to_chk:
        if day in booked:
            return excl

    # Book these days
    new_booked = booked.union(to_chk)
    incl = reward + fn(i + 1, frozenset(new_booked))

    return max(excl, incl)

print(fn(0, frozenset()))
```

### Pros:

* Purely functional state → works with `lru_cache`.
* Minimal changes to original logic.

### Cons:

* Memory blows up if days are large (since state stores actual days).
* Still exponential in worst case.

---

## **2. Memoizing by Encoding `booked` into a Bitmask**

Only viable if days are small (like $\leq 30$ for bitmask in an `int`):

```python
from functools import lru_cache

n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

@lru_cache(None)
def fn(i, booked_mask):
    if i == n:
        return 0

    # Skip
    excl = fn(i + 1, booked_mask)

    start, end, reward = mat[i]
    mask_needed = 0
    for d in range(start, end + 1):
        if (booked_mask >> d) & 1:
            return excl
        mask_needed |= (1 << d)

    incl = reward + fn(i + 1, booked_mask | mask_needed)
    return max(excl, incl)

print(fn(0, 0))
```

---

## **3. Replace Days with Project Index Constraints**

If the goal is just to make this memoizable **for large days** (like CSES constraints), you need to:

* Sort projects by start time
* In recursion, store only `(i, last_taken_end_time)` instead of the `booked` set
* This becomes **Weighted Interval Scheduling DP** which is $O(n \log n)$.

That’s the only way to make it scale to `n = 2 * 10^5`.

---


