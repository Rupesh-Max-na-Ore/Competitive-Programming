You're absolutely right again — the issue lies in the **`while True` input loop** of your `read_board()` function. In interactive input, unless you **signal end-of-input**, it will keep waiting forever. That’s why it feels like an "infinite loop."

---

### ✅ 🔧 Fix Options

#### ✅ **Option 1: Ask user for number of rows**

This is the **cleanest and most recommended** option. Modify your prompt to also ask for the number of rows:

```python
def read_board():
    k = int(input("Enter no. of queens: "))
    r = int(input("Enter number of rows in board: "))
    
    print("Enter Board:")
    board = []
    for _ in range(r):
        row = input().strip()
        board.append(row)

    return k, board
```

Now your test input looks like:

```
Enter no. of queens: 6
Enter number of rows in board: 8
Enter Board:
.......
.g.....
..*....
*......
.......
.....**
...*...
.......
```

#### ✅ **Option 2: Use a sentinel (e.g., 'END')**

You can keep reading rows until a line like `"END"` is entered:

```python
def read_board():
    k = int(input("Enter no. of queens: "))

    print("Enter Board (type END to stop):")
    board = []
    while True:
        row = input()
        if row.strip().upper() == "END":
            break
        if not row.strip():
            continue
        board.append(row.strip())

    return k, board
```

Now your test input looks like:

```
Enter no. of queens: 6
Enter Board (type END to stop):
.......
.g.....
..*....
*......
.......
.....**
...*...
.......
END
```

---

### 🚫 Why the original version fails

In a typical terminal, Python’s `input()` keeps waiting forever for new input unless:

* A `Ctrl+D` (Unix/Linux/macOS) or `Ctrl+Z + Enter` (Windows) is typed to raise an EOFError, or
* The input stream is closed (e.g., via redirect or IDE behavior).

This is not friendly for regular usage.

---

Would you like me to plug this into your full `n-queens` solver now?
