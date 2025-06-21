Yes! You can generate all **unique permutations of a string iteratively** using Python’s standard libraries or custom logic.

---

### ✅ 1. **Using `itertools.permutations` (Built-in, Fast, Simple)**

```python
from itertools import permutations

def solve(s):
    perms = set(permutations(s))  # removes duplicates
    sorted_perms = sorted("".join(p) for p in perms)

    print(len(sorted_perms))
    for p in sorted_perms:
        print(p)

s = input()
solve(s)
```

* **Pros:** Clean, concise, fast enough for small `n` (like ≤ 8).
* **Cons:** Generates duplicates first (slightly inefficient).

---

### ✅ 2. **Custom Iterative Algorithm (Heap's Algorithm Variant)**

Heap’s algorithm is a common iterative method to generate permutations, especially efficient for **all** permutations (not necessarily unique). To adapt it for **unique** permutations, we’ll need a set or frequency map to skip duplicates.

Here’s an iterative **set-based approach**:

```python
def solve(s):
    from collections import deque

    s = sorted(s)  # ensure lex order
    queue = deque([("", s)])
    seen = set()
    result = []

    while queue:
        prefix, chars = queue.popleft()
        if not chars:
            result.append(prefix)
            continue

        used = set()  # avoid duplicate choices at the same position
        for i, ch in enumerate(chars):
            if ch in used:
                continue
            used.add(ch)

            next_prefix = prefix + ch
            next_chars = chars[:i] + chars[i+1:]
            queue.append((next_prefix, next_chars))

    print(len(result))
    for p in result:
        print(p)

s = input()
solve(s)
```

* **Pros:** No recursion, handles uniqueness efficiently, outputs in lex order.
* **Cons:** More lines, a bit slower than the recursive version for `n = 8`.

---

### 🧠 Which One Should You Use?

| Method                   | Use When                                 | Notes                                 |
| ------------------------ | ---------------------------------------- | ------------------------------------- |
| `itertools.permutations` | Want fast prototype, tolerate duplicates | Add `set()` to remove duplicates      |
| Recursive (DFS)          | Need control, clarity, low memory        | Best overall for n ≤ 8                |
| Custom Iterative (Queue) | Avoid recursion, simulate DFS/BFS        | Slower, but safe from recursion depth |

Let me know if you want a Heap’s algorithm version too!
