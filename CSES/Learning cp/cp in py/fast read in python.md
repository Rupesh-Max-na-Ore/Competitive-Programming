That happens because

```python
input = sys.stdin.read
```

will **keep waiting** until it reaches *end-of-file (EOF)* —
it doesn’t stop after reading just 4 lines.

On CSES, this is fine because the platform sends **all input at once** and closes the stream,
but if you run it manually in your terminal, Python will just keep blocking until you press <kbd>Ctrl</kbd>+<kbd>D</kbd> (Linux/macOS) or <kbd>Ctrl</kbd>+<kbd>Z</kbd> then <kbd>Enter</kbd> (Windows)
to signal EOF.

---

### Two fixes

#### **1. Keep `sys.stdin.read` (fastest)**

You just need to provide *all* the input in one go, or paste it and press EOF:

```bash
python3 program.py <<EOF
4
2 4 4
3 6 6
6 8 2
5 7 3
EOF
```

#### **2. Use normal `input()` in a loop** (simpler for local testing)

```python
n = int(input())
projects = [tuple(map(int, input().split())) for _ in range(n)]
```

This stops after reading exactly `n` lines.

---

For CSES, the `sys.stdin.read` version is still better for speed with `n = 2 * 10^5`.
When testing locally, just remember to send EOF or switch to loop-based reading.

If you want, I can rewrite the **optimal Projects solution** using normal `input()` so it works identically both locally and on CSES.

---

What is EOF?

EOF stands for **End Of File** — it’s a special signal sent to a program to say:

> “There’s no more input coming; you can stop reading now.”

When you do

```bash
python3 program.py <<EOF
4
2 4 4
3 6 6
6 8 2
5 7 3
EOF
```

you’re using a **here-document** in the shell:

* Everything between the two `EOF` markers is fed to your program as if it were typed from standard input (`stdin`).
* When the shell reaches the second `EOF`, it sends the **EOF signal** to the program, and `sys.stdin.read()` stops blocking.

---

### When you type interactively

If you’re running your Python script and using `sys.stdin.read()`:

* Python will keep waiting for input until it receives the EOF signal.
* You send EOF manually with:

  * **Linux/macOS:** <kbd>Ctrl</kbd>+<kbd>D</kbd>
  * **Windows:** <kbd>Ctrl</kbd>+<kbd>Z</kbd> then <kbd>Enter</kbd>

Without EOF, `sys.stdin.read()` doesn’t know you’re done entering data.

---

If you want, I can show you exactly how this EOF signal interacts with `sys.stdin.read()` in Python, using a short experiment.

---

I see the problem — when you write:

```bash
python3 program.py <<EOF 4 2 4 4 3 6 6 6 8 2 5 7 3 EOF
```

the shell is **not** treating that as a proper *here-document*, because `EOF` must be **on its own line**, and so must the closing marker.

The correct syntax is:

```bash
python3 program.py <<EOF
4
2 4 4
3 6 6
6 8 2
5 7 3
EOF
```

Key points:

* `<<EOF` starts the here-document.
* You press Enter, then type your input exactly as the program expects.
* You put `EOF` on a **separate line by itself** to signal the end of input.

If you keep `EOF` on the same line as your data, the shell thinks the marker is part of your input, and the here-document never closes — so your program is stuck waiting for EOF.

If you’re running interactively and not using a here-document, you need to send:

* **Linux/macOS:** <kbd>Ctrl</kbd>+<kbd>D</kbd>
* **Windows (cmd):** <kbd>Ctrl</kbd>+<kbd>Z</kbd> then <kbd>Enter</kbd>

Do you want me to show you a clean version of your CSES *Projects* solution that reads input without getting stuck like this?
