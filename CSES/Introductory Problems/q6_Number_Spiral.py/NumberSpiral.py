"""
Number Spiral

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Number Spiral




addEventListener("DOMContentLoaded", function (e) {
    const mathElements = document.getElementsByClassName("math");
    const macros = {};
    for (let element of mathElements) {
        katex.render(element.textContent, element, {
            displayMode: element.classList.contains("math-display"),
            throwOnError: false,
            globalGroup: true,
            macros,
        });
    }
});


Time limit: 1.00 s
Memory limit: 512 MB



A number spiral is an infinite grid whose upper-left square has number 1. Here are the first five layers of the spiral:

Your task is to find out the number in row y and column x.
Input
The first input line contains an integer t: the number of tests.
After this, there are t lines, each containing integers y and x.
Output
For each test, print the number in row y and column x.
Constraints

1 \le t \le 10^5
1 \le y,x \le 10^9

Example
Input:
3
2 3
1 1
4 2

Output:
8
1
15
"""
import sys
input = sys.stdin.read

def spiral(r,c):
    if(r==c):
        return r*r - (r-1)
    elif(r>c):
        d=r
        diag = d*d - (d-1)
        if d % 2 == 0:
            return diag + r - c
        else:
            return diag - r + c
    else:
        d=c
        diag = d*d - (d-1)
        if d % 2 == 0:
            return diag + r - c
        else:
            return diag - r + c
        
data = input().split()
t = int(data[0])
res = []
idx = 1
for _ in range(t):
    r = int(data[idx])
    c = int(data[idx + 1])
    res.append(str(spiral(r, c)))
    idx += 2

sys.stdout.write('\n'.join(res) + '\n')

"""
Absolutely! Let's walk step by step through how the final code handles **extracting and processing multiple queries efficiently**, especially using **fast input and output**:

---

## ✅ Problem Recap:

* You're given `t` queries.
* Each query is a pair of integers `y` and `x`.
* For each pair, compute the value at position `(y, x)` in a number spiral.
* **Constraints**: Up to `10^5` queries, so speed is important.

---

## 🔍 Step-by-step Breakdown of Input Handling:

```python
import sys
input = sys.stdin.read
```

* Instead of reading input line by line (`input()`), we use `sys.stdin.read()` to **read all input at once**.
* This is much faster for large input sizes.
* The result is a single string with all the input text.

---

```python
data = input().split()
```

* `.split()` splits that big string into a **list of strings** (separated by whitespace).
* For example, if input was:

  ```
  3
  2 3
  1 1
  4 2
  ```

  Then `data` becomes:

  ```python
  ['3', '2', '3', '1', '1', '4', '2']
  ```

---

```python
t = int(data[0])
```

* First element is the number of test cases `t`.

---

```python
res = []
idx = 1
for _ in range(t):
    y = int(data[idx])
    x = int(data[idx + 1])
    res.append(str(spiral(y, x)))
    idx += 2
```

### Here's what happens:

* `idx = 1` starts right after `t`.
* Loop runs `t` times.
* For each iteration:

  * `y` and `x` are extracted from `data` at positions `idx` and `idx + 1`.
  * `spiral(y, x)` computes the answer for the current query.
  * Convert result to `str` and append to result list.
  * Increment index by 2 to move to the next pair.

---

## ✅ Output Handling:

```python
sys.stdout.write('\n'.join(res) + '\n')
```

* All answers are joined into one string separated by newlines (`\n.join(...)`).
* Output is printed at once using `sys.stdout.write(...)`.
* Much faster than calling `print()` in each iteration for large outputs.

---

## 🔁 Summary:

| Step                 | Action                           | Why                     |
| -------------------- | -------------------------------- | ----------------------- |
| `sys.stdin.read()`   | Read all input at once           | Fast input              |
| `input().split()`    | Break into tokens                | Easy indexing           |
| Loop with `idx += 2` | Extract `y, x` pairs efficiently | Handles 10⁵ inputs fast |
| `sys.stdout.write()` | Print all at once                | Fast output             |

---

Let me know if you’d like to visualize how the spiral numbering works or trace through one sample input step by step.

"""