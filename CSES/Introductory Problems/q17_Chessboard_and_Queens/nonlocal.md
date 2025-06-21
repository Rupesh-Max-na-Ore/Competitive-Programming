In Python, the `nonlocal` keyword is used **inside nested functions** to indicate that a variable refers to a variable in the **nearest enclosing (non-global) scope** — not the global one.

---

### 📌 Use Case:

When you have a function inside another function and want the inner function to modify a variable defined in the outer function (but not global), you use `nonlocal`.

---

### 🔍 Example:

```python
def outer():
    count = 0  # this is in the enclosing scope

    def inner():
        nonlocal count  # refers to 'count' in outer(), not a new local one
        count += 1
        print("Inner count:", count)

    inner()
    inner()
    print("Outer count:", count)

outer()
```

🟢 **Output:**

```
Inner count: 1
Inner count: 2
Outer count: 2
```

Without `nonlocal`, the `count` inside `inner()` would be considered a **new local variable**, and trying to modify it would cause an `UnboundLocalError` if you tried `count += 1`.

---

### 🚫 Difference from `global`:

* `nonlocal` → modifies variables in the nearest **enclosing function** scope.
* `global` → modifies variables in the **global (module-level)** scope.

---

Let me know if you want to visualize this with a memory diagram or try it in a practical example like counting valid N-Queens paths!
