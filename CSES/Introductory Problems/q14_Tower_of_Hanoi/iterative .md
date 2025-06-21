Implementing the **Tower of Hanoi** iteratively is a fascinating exercise. While the recursive solution is simple and elegant, the **iterative solution** requires a bit more work but can be done using a **stack simulation** or based on known algorithms.

---

## ✅ Iterative Tower of Hanoi (Using Known Pattern for 3 Pegs)

The **key idea** for 3 pegs is:

* There are always **$2^n - 1$** moves.
* The **rules of movement differ** depending on whether `n` is even or odd.

---

### 🔄 Algorithm Overview

1. Number the pegs:

   * Source: 1
   * Auxiliary: 2
   * Destination: 3

2. If `n` is **even**, **swap the auxiliary and destination** pegs.

3. Repeat for $2^n - 1$ moves:

   * On **move i**:

     * If `i % 3 == 1`: Move between source and destination.
     * If `i % 3 == 2`: Move between source and auxiliary.
     * If `i % 3 == 0`: Move between auxiliary and destination.

---

### 🧠 Helper Function to Move Disks Between Pegs

You’ll need to simulate three stacks (lists) and always ensure a **smaller disk is never placed on a larger one**.

---

### 🧑‍💻 Python Implementation

```python
def move_disk(from_peg, to_peg, from_label, to_label):
    if not from_peg:
        disk = to_peg.pop()
        from_peg.append(disk)
        print(f"{to_label} {from_label}")
    elif not to_peg:
        disk = from_peg.pop()
        to_peg.append(disk)
        print(f"{from_label} {to_label}")
    elif from_peg[-1] > to_peg[-1]:
        disk = to_peg.pop()
        from_peg.append(disk)
        print(f"{to_label} {from_label}")
    else:
        disk = from_peg.pop()
        to_peg.append(disk)
        print(f"{from_label} {to_label}")

def iterative_tower_of_hanoi(n):
    total_moves = 2**n - 1
    src = list(range(n, 0, -1))
    aux = []
    dst = []

    if n % 2 == 0:
        aux_label, dst_label = 3, 2
    else:
        aux_label, dst_label = 2, 3

    print(total_moves)
    for i in range(1, total_moves + 1):
        if i % 3 == 1:
            move_disk(src, dst, 1, dst_label)
        elif i % 3 == 2:
            move_disk(src, aux, 1, aux_label)
        else:
            move_disk(aux, dst, aux_label, dst_label)

# Example:
n = int(input())
iterative_tower_of_hanoi(n)
```

---

### 🧠 Time & Space Complexity

* **Time:** $O(2^n)$
* **Space:** $O(n)$ for storing pegs (stacks)

---

### ✅ Output Example (n = 2)

```
3
1 2
1 3
2 3
```

---

Want a **non-stack-based simulation** version next? Or a **bitwise iterative formula** version (exists for advanced usage)?

Great! Let's explore both:

---

## ✅ 1. **Non-Stack-Based Simulation (Using Peg Numbers Only)**

This approach doesn’t simulate actual stacks but **prints the moves directly** using a formulaic rule. It's simpler but assumes you're not interested in tracking disk states.

### 🧠 Key Idea

For `n` disks, make $2^n - 1$ moves using modulo math. This follows the **legal move pattern**.

### 🔢 Algorithm

1. Number pegs:

   * Source: `1`
   * Auxiliary: `2`
   * Destination: `3`

2. If `n` is even, swap the destination and auxiliary.

3. For each move `i` from `1` to `2^n - 1`:

   * `i % 3 == 1`: move between source and destination
   * `i % 3 == 2`: move between source and auxiliary
   * `i % 3 == 0`: move between auxiliary and destination

### 🧑‍💻 Code

```python
def non_stack_tower_of_hanoi(n):
    total_moves = 2 ** n - 1
    src, aux, dst = 1, 2, 3

    # If number of disks is even, swap aux and dst
    if n % 2 == 0:
        aux, dst = dst, aux

    print(total_moves)
    for i in range(1, total_moves + 1):
        if i % 3 == 1:
            print(f"{src} {dst}")
        elif i % 3 == 2:
            print(f"{src} {aux}")
        else:
            print(f"{aux} {dst}")

# Example
n = int(input())
non_stack_tower_of_hanoi(n)
```

### ❗ Limitation

This does **not** track which disk is moved — only **legal peg transitions** are printed. It’s valid for CSES and many problems that don’t care about tracking state.

---

## ✅ 2. **Bitwise Iterative Tower of Hanoi** (Advanced & Elegant)

This approach uses bitwise logic to **determine which disk moves on each turn**.

### 🤯 Insight

* Disk `k` (1-based) moves at steps where `i % 2^k == 0`.
* Only **one disk** moves per step.
* You can determine the disk being moved using `i & -i`.

### 🧑‍💻 Bitwise Hanoi Implementation

```python
def bitwise_tower_of_hanoi(n):
    total_moves = 2 ** n - 1
    print(total_moves)

    pegs = [1, 2, 3]
    if n % 2 == 0:
        pegs[1], pegs[2] = pegs[2], pegs[1]  # Swap aux and dst

    positions = [0] * (n + 1)  # Disk position: pegs[positions[disk]]

    for move in range(1, total_moves + 1):
        # Find which disk to move
        disk = (move & -move).bit_length()  # i & -i gives the lowest set bit
        from_peg = pegs[positions[disk]]
        positions[disk] = (positions[disk] + 1) % 3
        to_peg = pegs[positions[disk]]
        print(f"{from_peg} {to_peg}")

# Example
n = int(input())
bitwise_tower_of_hanoi(n)
```

### 🔍 Explanation

* `move & -move` isolates the **least significant bit** → determines which disk to move.
* Disk positions rotate among pegs in a consistent cycle.
* The position of each disk is tracked in `positions`.

---

## 🧠 Time and Space Complexity

All methods:

* **Time:** $O(2^n)$ — number of moves
* **Space:**

  * Non-stack version: $O(1)$
  * Bitwise version: $O(n)$ — tracks positions
  * Stack version: $O(n)$ — uses lists to simulate pegs

---

Would you like to visualize disk movement too or animate it (textually or graphically)?

Yes — the **intuition** behind why 3 pegs work (and are sufficient) for the **Tower of Hanoi** lies in a combination of **recursive divide-and-conquer strategy** and **freedom of movement**.

Let’s break it down:

---

## 🧠 Why Three Pegs Work: Core Intuition

Imagine you have to move a tower of `n` disks from Peg A to Peg C using Peg B as temporary storage, with the constraint:
🔴 You can only move **one disk at a time**, and
🔴 You can **never place a larger disk on a smaller one**.

The 3 pegs provide just enough flexibility to:

1. Temporarily store smaller disks,
2. Free up the largest disk,
3. Reconstruct the tower elsewhere **in the correct order**.

---

## 🔄 Recursive Strategy

Here's how it works recursively (and why 3 pegs are sufficient):

1. **Move top (n-1) disks from A to B** — *using C as auxiliary*.
2. **Move the largest disk (disk n) from A to C** — this is a direct move.
3. **Move the (n-1) disks from B to C** — *using A as auxiliary*.

Every recursive step only needs **3 pegs** to temporarily hold and rearrange disks.

### 🔁 Key Point:

The moment you divide the task into subproblems, you reuse the 3 pegs **in a rotating role** (source, target, auxiliary) at every recursive level.

---

## 🧩 What If There Were Only 2 Pegs?

* ❌ You **cannot solve** the problem for `n > 1` using only **2 pegs**.
* Why? You would have to place at least one disk somewhere **other than the target** temporarily — but you have nowhere to put it.

So:

* **1 peg**: trivial, not even a puzzle.
* **2 pegs**: insufficient for rearranging.
* ✅ **3 pegs**: just enough for a recursive escape route.

---

## 💡 Mathematical Analogy

Three pegs allow you to implement a **binary recursive tree** of moves:

* Total moves = $2^n - 1$
* At every level, you're breaking the problem into 2 subproblems of size $n - 1$

So the structure of the **recursive algorithm aligns perfectly** with the number of pegs.

---

## ⚖️ Efficiency

Interestingly, **3 pegs is not optimal for larger `n`** if you are allowed *more* pegs (like 4 or more). This leads to the **Frame-Stewart algorithm**, which reduces the number of moves using more storage pegs — but becomes very complex.

---

## 🎯 Summary

| Feature                     | 3 Pegs |
| --------------------------- | ------ |
| Can solve for any `n`       | ✅ Yes  |
| Efficient for small `n`     | ✅ Yes  |
| Enables recursive breakdown | ✅ Yes  |
| Mirrors binary recursion    | ✅ Yes  |

So 3 pegs are **just enough** for Tower of Hanoi to work, but they work beautifully due to the elegance of recursive thinking.

---

Want to try solving it for 4 pegs next and compare?
