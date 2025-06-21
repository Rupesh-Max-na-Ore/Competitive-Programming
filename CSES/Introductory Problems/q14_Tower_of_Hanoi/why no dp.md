Great question.

### 🔁 Can we use **memoization** for Tower of Hanoi?

Technically: **Yes, you can memoize** the function `toh(n, a, b, c)` (i.e., cache results of function calls).

But practically and **performance-wise**, **memoization is not worth it** for this problem.

---

### ⚙️ Why?

Let’s analyze:

#### ✅ What memoization helps with:

Memoization is useful when:

* The problem has **overlapping subproblems** (same inputs computed repeatedly).
* You want to **avoid recomputation** by caching previously computed results.

#### ❌ Tower of Hanoi doesn't really benefit:

In Tower of Hanoi:

* Even though the recursive calls are similar in structure, each call is made with **different parameters** (e.g., different `from`, `to`, `aux` pegs).
* Each step in the recursion performs **distinct moves** — it doesn't **reuse any state**.
* So, **there is little to no overlapping subproblems**.

---

### ⏱ Time and 🧠 Space Complexity:

| Approach         | Time Complexity | Space Complexity                                             |
| ---------------- | --------------- | ------------------------------------------------------------ |
| Plain recursion  | $O(2^n)$        | $O(n)$ (recursion stack)                                     |
| With memoization | Still $O(2^n)$  | Worse: $O(n \cdot 3!)$ if you cache each `(n, a, b, c)` call |

* Memoization adds overhead without reducing the fundamental exponential growth.
* You’d be storing all calls of the form `(n, source, aux, dest)` → **a lot of combinations**.

---

### 🧠 Verdict:

* ✅ **Correctness-wise:** Memoization is possible.
* ❌ **Performance-wise:** Not helpful. The subproblems are unique, so memoizing them just wastes memory and adds complexity.
* 🧩 **Better idea:** For optimization, use **iterative** versions or **bit-based representations** (like for massive state machines) — but even those don’t beat $2^n$ in worst case.

---

Let me know if you want to **see what a memoized version looks like anyway**, just for learning!
