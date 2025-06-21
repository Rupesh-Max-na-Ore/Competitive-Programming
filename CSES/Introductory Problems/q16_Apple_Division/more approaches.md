Great! Here's a **more optimized version** of the Apple Division problem.

---

### ✅ Optimization Idea:

Instead of maintaining two full lists (`fst` and `scnd`), we:

* Keep a single running total `group1_sum`
* Compute the total sum once at the beginning
* The other group’s sum becomes `total_sum - group1_sum`

This eliminates the need to store and sum two separate lists at every step — drastically improving performance.

---

### ⚡ Optimized Code:

```python
def divide(i, n, lst, group1_sum, total_sum, min_diff):
    if i == n:
        group2_sum = total_sum - group1_sum
        diff = abs(group1_sum - group2_sum)
        if diff < min_diff[0]:
            min_diff[0] = diff
        return
    
    # Include lst[i] in group 1
    divide(i + 1, n, lst, group1_sum + lst[i], total_sum, min_diff)
    # Include lst[i] in group 2 (implicitly, by skipping it from group 1)
    divide(i + 1, n, lst, group1_sum, total_sum, min_diff)

def solve(n, lst):
    total_sum = sum(lst)
    min_diff = [float('inf')]
    divide(0, n, lst, 0, total_sum, min_diff)
    return min_diff[0]

# Input handling
n = int(input())
lst = list(map(int, input().split()))
print(solve(n, lst))
```

---

### ✅ Benefits:

* **Time Complexity:** Still $O(2^n)$, but faster in practice.
* **Space Complexity:** Reduced to $O(n)$ due to the elimination of two growing lists.
* **More readable** and avoids unnecessary summation operations inside the recursion.

---

Let me know if you want a **bitmask or DP approach** too — for even more advanced control!

Great! Let’s go through **multiple approaches** to solve the Apple Division problem and how they scale — especially if you're aiming to solve harder variants with tighter constraints (e.g., larger `n` or more optimization).

---

## 🔁 **Problem Summary**

Given `n` apples with weights, divide them into two groups to minimize the **absolute difference of group sums**.

---

## ✅ Approach 1: **Brute Force Backtracking**

Already discussed.

* Time: $O(2^n)$
* Works up to $n \leq 20$
* Pros: Easy to implement
* Cons: Explodes for larger `n`

---

## ✅ Approach 2: **Bitmask Enumeration**

Instead of recursion, loop through all bitmasks from `0` to `2^n - 1`.

```python
def solve(n, lst):
    total = sum(lst)
    min_diff = float('inf')
    for mask in range(1 << n):
        group1 = 0
        for i in range(n):
            if mask & (1 << i):
                group1 += lst[i]
        group2 = total - group1
        min_diff = min(min_diff, abs(group1 - group2))
    return min_diff

# Input
n = int(input())
lst = list(map(int, input().split()))
print(solve(n, lst))
```

* Time: $O(n \cdot 2^n)$
* Still works well for $n \leq 20$
* Slightly faster than recursion due to no function calls

---

## 🚀 Approach 3: **Meet in the Middle (for $n \leq 40$)**

Split into 2 halves. Compute all subset sums for each half, and use binary search to find best pair.

```python
import bisect

def get_subsets(nums):
    n = len(nums)
    res = []
    for mask in range(1 << n):
        total = 0
        for i in range(n):
            if mask & (1 << i):
                total += nums[i]
        res.append(total)
    return res

def solve(n, lst):
    half = n // 2
    left = lst[:half]
    right = lst[half:]
    total = sum(lst)
    lsubs = get_subsets(left)
    rsubs = get_subsets(right)
    rsubs.sort()
    
    min_diff = float('inf')
    for ls in lsubs:
        target = total // 2 - ls
        idx = bisect.bisect_left(rsubs, target)
        for j in [idx - 1, idx]:
            if 0 <= j < len(rsubs):
                group1 = ls + rsubs[j]
                group2 = total - group1
                min_diff = min(min_diff, abs(group1 - group2))
    return min_diff

n = int(input())
lst = list(map(int, input().split()))
print(solve(n, lst))
```

* Time: $O(2^{n/2} \cdot \log 2^{n/2}) = O(2^{n/2} \cdot n)$
* Handles up to $n = 40$
* Uses extra space for storing subset sums

---

## ⚡ Approach 4: **Dynamic Programming (Pseudo-polynomial)**

If weights are small integers, use subset-sum-style DP.

```python
def solve(n, lst):
    total = sum(lst)
    dp = [False] * (total + 1)
    dp[0] = True

    for weight in lst:
        for i in range(total, weight - 1, -1):
            dp[i] |= dp[i - weight]

    min_diff = float('inf')
    for i in range(total + 1):
        if dp[i]:
            diff = abs((total - i) - i)
            min_diff = min(min_diff, diff)
    return min_diff
```

* Time: $O(n \cdot \text{sum})$
* Space: $O(\text{sum})$
* Only works well if sum of weights $\leq 10^5$ or so

---

## 🔥 Advanced: Optimized DP with Bitset (C++ only normally, but simulated via Python set)

Use `set` or `bitset` tricks to optimize memory. Can implement with `set` of reachable sums to simulate bitset behavior.

---

## 🎯 Summary Table:

| Approach            | Time Complexity  | Max `n`           | Notes                      |
| ------------------- | ---------------- | ----------------- | -------------------------- |
| Backtracking        | $O(2^n)$         | ≤ 20              | Basic recursion            |
| Bitmask             | $O(n \cdot 2^n)$ | ≤ 20              | Fastest brute              |
| Meet in the Middle  | $O(2^{n/2})$     | ≤ 40              | Smart strategy             |
| Subset Sum DP       | $O(n \cdot S)$   | High if sum small | Only if weights are small  |
| Bitset Optimization | $O(n \cdot S)$   | C++-friendly      | Python simulation possible |

---

Let me know:

* Which variant you want to focus on for practice?
* Want to try the multi-threaded version (parallel bitmasking)?
* Want to adapt this for **3-group split** (advanced version)?

