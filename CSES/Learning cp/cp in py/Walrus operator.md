# Walrus notation in python and its uses?

The **walrus operator** in Python is written as `:=` and is formally known as the **assignment expression** operator. It was introduced in **Python 3.8** (PEP 572).

---

### 🔧 **Formal Definition**

Let $x := expr$ denote an **assignment expression**, which:

* Evaluates `expr`
* Assigns its value to the variable `x`
* Returns the value

This allows **assigning a value to a variable as part of an expression**.

---

### ✅ **Syntax**

```python
variable := expression
```

---

### 📌 **Use Cases**

#### 1. **While Loops with In-Place Assignment**

Traditional:

```python
line = input()
while line != "quit":
    print(f"You entered: {line}")
    line = input()
```

With walrus:

```python
while (line := input()) != "quit":
    print(f"You entered: {line}")
```

✔ Reduces duplication (`input()`).

---

#### 2. **List Comprehension with Filtering**

Traditional:

```python
results = []
for x in data:
    y = expensive_operation(x)
    if y > 0:
        results.append(y)
```

With walrus:

```python
results = [y for x in data if (y := expensive_operation(x)) > 0]
```

✔ More concise, avoids redundant calls.

---

#### 3. **Read-And-Test Pattern**

```python
# Read lines from a file until EOF
while (line := file.readline()):
    process(line)
```

✔ Assign and test in a single expression.

---

#### 4. **Repeated Subexpression Avoidance**

```python
if (n := len(some_list)) > 10:
    print(f"List is too long ({n} elements)")
```

✔ Avoids computing `len(some_list)` twice.

---

### ⚠️ **Things to Keep in Mind**

* Only available in **Python 3.8+**
* Should **not be overused**, especially if it hurts readability
* Cannot be used in **assignment statements** like:

  ```python
  x := 5  # ❌ SyntaxError
  ```

  Must be **inside** an expression:

  ```python
  if (x := 5):  # ✅ Valid
      ...
  ```

---

### 📚 Example: Regex Matching

```python
import re
pattern = re.compile(r"\d+")
if (match := pattern.search("Value: 42")):
    print("Found:", match.group())
```

---

### Summary Table

| Use Case            | Benefit                        |
| ------------------- | ------------------------------ |
| Input loops         | Avoid repeated code            |
| List comprehensions | Inline filtering & computation |
| Avoid recomputation | Reduce expensive calls         |
| File reading        | Read and test in one line      |

---

Would you like a mathematical or compiler-design perspective on how this fits into Python’s grammar, or examples of how it might compare to assignment in functional or lazy languages?
