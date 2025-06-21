The **exact time complexity** of the Tower of Hanoi problem for `n` disks is:

---

### ✅ **Time Complexity:**

$$
T(n) = 2^n - 1
$$

---

### 🔍 **Explanation (Recurrence Relation):**

The recursive steps follow this pattern:

* Move `n-1` disks from source to auxiliary.
* Move the `n`th (largest) disk from source to destination.
* Move `n-1` disks from auxiliary to destination.

So the recurrence is:

$$
T(n) = 2T(n-1) + 1
$$

Solving it:

* $T(1) = 1$
* $T(2) = 2T(1) + 1 = 3$
* $T(3) = 2T(2) + 1 = 7$
* ...

This is a classic recurrence that solves to:

$$
T(n) = 2^n - 1
$$

---

### ⏱ **So Time Complexity:**

* **Exact:** $2^n - 1$
* **Big-O:** $\boxed{O(2^n)}$

---

### 🧠 Insight:

* For each disk added, the number of moves **doubles** plus one extra move.
* That’s why this problem becomes impractical for large `n` (e.g., $n = 64$ → over 18 quintillion moves!).

Let me know if you'd like a derivation or visualization of this recurrence solution.
