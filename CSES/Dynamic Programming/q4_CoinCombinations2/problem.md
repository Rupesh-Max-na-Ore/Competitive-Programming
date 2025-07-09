CSES Problem Set
      Coin Combinations II

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Coin Combinations II




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



Consider a money system consisting of n coins. Each coin has a positive integer value. Your task is to calculate the number of distinct ordered ways you can produce a money sum x using the available coins.
For example, if the coins are \{2,3,5\} and the desired sum is 9, there are 3 ways:

2+2+5
3+3+3
2+2+2+3

Input
The first input line has two integers n and x: the number of coins and the desired sum of money.
The second line has n distinct integers c_1,c_2,\dots,c_n: the value of each coin.
Output
Print one integer: the number of ways modulo 10^9+7.
Constraints

1 \le n \le 100
1 \le x \le 10^6
1 \le c_i \le 10^6

Example
Input:
3 9
2 3 5

Output:
3


what is wrong here: def ways(i, s, coins, dp):
    if s == 0:
        return 1
    if i < 0 or s < 0:
        return 0
    if dp[s] != -1:
        return dp[s]
    # not pick ith coin and move to next coin or pick it and stay here 
    dp[s] = ways(i - 1, s, coins, dp) + ways(i, s - coins[i], coins, dp)
    return dp[s]

n, sum = map(int, input().split())
curr = list(map(int, input().split()))
print(ways(n - 1, sum, curr, [-1]*(sum+1)))

Your implementation of the `ways` function intends to solve the **Coin Combinations II** problem (unordered multisets) using **memoized recursion**, but there is a **critical conceptual bug**:

---

## ❌ The Problem

You're using a **1D memoization array** `dp[s]`, which means:

* You are **ignoring the `i` index** in the cache.
* But the function's state actually depends on **both `i` and `s`**:

  $$
  \texttt{ways(i, s)} = \text{# of ways to form sum } s \text{ using first } i \text{ coin types}
  $$

Hence, caching only based on `s` is incorrect, because for different values of `i`, the number of ways to form sum `s` can differ.

---

## ✅ Solution: Use a 2D DP Array

You need to cache using both `i` and `s`, i.e., `dp[i][s]`.

---

## ✔️ Corrected Python Code

```python
def ways(i, s, coins, dp):
    if s == 0:
        return 1
    if i < 0 or s < 0:
        return 0
    if dp[i][s] != -1:
        return dp[i][s]

    # Exclude coin[i], move to i-1; or include it, stay at i
    dp[i][s] = ways(i - 1, s, coins, dp) + ways(i, s - coins[i], coins, dp)
    return dp[i][s]

n, sum_ = map(int, input().split())
curr = list(map(int, input().split()))
dp = [[-1] * (sum_ + 1) for _ in range(n)]
print(ways(n - 1, sum_, curr, dp))
```

---

### Optional: Add Modulo

If required by problem (like CSES):

```python
MOD = 10**9 + 7
dp[i][s] = (ways(i - 1, s, coins, dp) + ways(i, s - coins[i], coins, dp)) % MOD
```

---

## 🔍 Summary of Fixes

| Issue                 | Fix                      |
| --------------------- | ------------------------ |
| 1D memoization        | Change to 2D: `dp[i][s]` |
| Ignoring `i` in cache | Include `i` in cache key |
| Not handling modulo   | Add `% MOD` if needed    |

---

Would you also like the **bottom-up tabulated version** built from this top-down logic?

Let’s **formally derive** the solution for **Coin Combinations II** — where **order of coins doesn't matter** — starting from:

1. **Recursive formulation (naive)**
2. **Memoization (top-down DP)**
3. **Tabulation (bottom-up DP)**

We will build from first principles. This is a **classical unbounded knapsack** problem.

---

## 🔢 Problem

Given coins $c_1, c_2, \dots, c_n$ and a target sum $x$, count the number of ways to sum to $x$, **using each coin any number of times**, **but order does not matter**.

---

## Step 1: 🔁 Recursive Formulation (Without Memoization)

### 📌 Subproblem

Let:

$$
\text{ways}(i, s) = \text{Number of ways to make sum } s \text{ using first } i \text{ coin types}
$$

We define a recursive function:

* Include coin `i`: stay at `i`, and reduce sum by `coins[i]`
* Exclude coin `i`: move to `i-1`, same sum

### 💡 Recurrence:

$$
\text{ways}(i, s) =
\begin{cases}
1 & \text{if } s = 0 \\
0 & \text{if } i < 0 \text{ or } s < 0 \\
\text{ways}(i-1, s) + \text{ways}(i, s - coins[i]) & \text{otherwise}
\end{cases}
$$

### 🧪 Python-style Recursive Code

```python
def ways(i, s):
    if s == 0:
        return 1
    if i < 0 or s < 0:
        return 0
    return ways(i - 1, s) + ways(i, s - coins[i])
```

### ❌ Problem: Exponential Time $O(2^n \cdot x)$

---

## Step 2: 🧠 Add Memoization (Top-Down DP)

We cache previously computed subproblems using a dictionary or 2D array.

```python
from functools import lru_cache

@lru_cache(None)
def ways(i, s):
    if s == 0:
        return 1
    if i < 0 or s < 0:
        return 0
    return ways(i - 1, s) + ways(i, s - coins[i])
```

### 🕒 Time Complexity: $O(n \cdot x)$

* $n$: number of coin types
* $x$: target sum

---

## Step 3: 📥 Tabulation (Bottom-Up DP)

We now reverse the recursion to build from base cases.

### 💡 State

Let `dp[i][s]` = number of ways to make sum `s` using first `i` coins.

But we can **optimize space** by using **1D dp**, since at step `i` we only need results from `i` or `i - 1`.

---

### 🚀 Final Optimized 1D Tabulation (Unordered multisets)

```python
def countWays(n, x, coins):
    MOD = 10**9 + 7
    dp = [0] * (x + 1)
    dp[0] = 1  # base: 1 way to make sum 0

    for coin in coins:
        for s in range(coin, x + 1):
            dp[s] = (dp[s] + dp[s - coin]) % MOD

    return dp[x]
```

---

### ✅ Why This Works

* We iterate over **coins first** → ensures each coin is considered only once per sum.
* This avoids double-counting permutations like `2+3+2`, `3+2+2`, etc.
* We build combinations in **increasing order**, naturally excluding order variations.

---

## 🔄 Comparison of Variants

| Variant              | Loop Order          | dp\[s] Update                      | Meaning                      |
| -------------------- | ------------------- | ---------------------------------- | ---------------------------- |
| Coin Combinations I  | `for s` then `coin` | all orders of coins (permutations) | Count ordered combinations   |
| Coin Combinations II | `for coin` then `s` | unordered combinations (multisets) | Count unordered combinations |

---

## 📘 Summary

| Step | Approach        | Description                                 | Time           | Space          |
| ---- | --------------- | ------------------------------------------- | -------------- | -------------- |
| 1    | Pure Recursion  | Try all include/exclude paths               | Exponential    | Stack depth    |
| 2    | Memoization     | Cache results to avoid recomputation        | $O(n \cdot x)$ | $O(n \cdot x)$ |
| 3    | Tabulation (1D) | Bottom-up iterative DP with coin-first loop | $O(n \cdot x)$ | $O(x)$         |

---

Would you like a full annotated Java version showing each step (recursion → memoization → tabulation) side by side?

tell me why do we need to consider 2d dp for memoization approach but only 1d for tabulation?

This is an **excellent and deep question**, touching on a key conceptual difference between **memoization (top-down)** and **tabulation (bottom-up)**.

We’ll analyze it carefully.

---

## ❓ Why do we need **2D DP** for **memoization**, but **only 1D** for **tabulation** in Coin Combinations II?

### Let’s formalize first.

We're solving:

> **Number of ways to make sum `x` using coins `c₁, ..., cₙ` (infinite supply), where order doesn’t matter.**

---

## 🧠 Top-Down (Memoization)

We define the recursive function as:

$$
\text{ways}(i, s) = \text{number of ways to make sum } s \text{ using coins } c_0 \text{ to } c_i
$$

* Decision: at `ways(i, s)`, we can:

  * Exclude `c_i`: call `ways(i-1, s)`
  * Include `c_i`: call `ways(i, s - c_i)`

Here, the **state** is fully characterized by **both**:

* `i`: how many coins (and which ones) you're allowed to use
* `s`: the remaining sum

Thus, we must **cache/memoize on both `(i, s)`**, leading to **2D DP**.

### 🔁 Why not 1D?

If you use just `dp[s]` and cache based only on `s`, then:

* The same `s` may be computed multiple times for different subsets of coins.
* So your cache can return **wrong values**, violating correctness.

✅ Therefore: **Memoization = 2D DP**

---

## 🔃 Bottom-Up (Tabulation)

Now let’s consider **bottom-up tabulation** for the same problem.

We initialize:

```python
dp[0] = 1  # base: one way to make sum 0
```

And then we do:

```python
for coin in coins:
    for s in range(coin, x + 1):
        dp[s] += dp[s - coin]
```

### ⚙️ Why this works with **1D dp**:

This loop structure ensures:

* You consider each `coin` **only once**, and then **add** its contribution to `dp[s]` for all sums.
* At each `s`, the value `dp[s]` is correctly built from smaller `s` values that **used only earlier coins**.

💡 Key trick: You process coins in the **outer loop**, and `s` in the **inner loop** (in increasing order). This means:

* At the time you're computing `dp[s]` with `coin c_i`, all contributions from `c_0 ... c_{i-1}` are already baked in.

So **you don’t need to store `(i, s)` explicitly**, because coin inclusion is naturally handled by the loop ordering.

✅ Therefore: **Tabulation = 1D DP**, if loop ordering is correct.

---

## 🔄 Summary Table

| Approach                   | State    | Storage Needed  | Explanation                                                                                  |
| -------------------------- | -------- | --------------- | -------------------------------------------------------------------------------------------- |
| **Memoization (Top-Down)** | `(i, s)` | `dp[i][s]` (2D) | You manually control inclusion/exclusion paths, so both `i` and `s` must be tracked in memo. |
| **Tabulation (Bottom-Up)** | Just `s` | `dp[s]` (1D)    | Loop ordering ensures coin selection happens correctly without explicit tracking of `i`.     |

---

## 🧪 Analogy

Think of it like **building a wall**:

* In **memoization**, you ask: *how can I build height `s` using bricks up to type `i`?* → You need to remember **which bricks you're allowed to use** = `i`.

* In **tabulation**, you build from the ground up. For each brick type, you lay all layers it can contribute to — naturally growing the structure, no need to track brick types explicitly.

---

Let me know if you'd like a visual or diagram to make this even more intuitive.
