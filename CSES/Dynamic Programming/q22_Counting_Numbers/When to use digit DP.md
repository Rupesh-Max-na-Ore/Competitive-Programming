How to know when to use digit dp? In OAs they expect us to code this in 20 minutes!

That’s the right pain point 😅 — digit DP looks “scary” when you first meet it, but there’s actually a **recognizable pattern**. Once you see it, you know immediately: *“Ah, this is digit DP.”*

Let’s break it down.

---

## 🔹 Hallmarks of Digit DP Problems

You should think **digit DP** when:

1. **The problem asks you to count numbers in a range** $[a,b]$.

   * Example: “Count numbers without repeated adjacent digits between a and b.”
   * Example: “Count numbers with digit sum divisible by 7 between a and b.”

2. **The constraint is up to 10^18 (or very large)**.

   * If $b$ is huge, you cannot loop through all numbers.
   * That’s the key: brute force impossible ⇒ need digit-level reasoning.

3. **The condition depends on digits, not the whole number**.

   * “No adjacent equal digits.”
   * “Digit sum ≤ K.”
   * “Contains at least one 7.”
   * “Digits are strictly increasing.”

   All of these can be tracked by small state variables.

4. **You can express the property as: `current digit choice` + `state from previous digits`**.

   * That’s exactly what digit DP does.

---

## 🔹 Skeleton of Digit DP

Once you detect it’s digit DP, you almost always use the same **DP state**:

```
dp(pos, prevState, tight, leading)
```

* `pos`: current digit index (0 … len-1).
* `prevState`: property tracker (last digit, digit sum so far, etc.).
* `tight`: are we still equal to prefix of limit or already smaller?
* `leading`: are we still in leading zeros?

And then:

1. Base case: if pos == n → return 1 if valid, else 0.
2. Transition: choose next digit from 0..limit.
3. Skip invalid digits (e.g., if equal to prev).
4. Memoize.

This skeleton is 90% reusable across problems.

---

## 🔹 How to Code Fast in OAs

You’re right: in an OA, you don’t have time to “derive” it from scratch. You need **muscle memory**.
Here’s how to get there:

1. **Practice 3–4 classic digit DP problems** until you can write the skeleton blindfolded:

   * Count numbers without consecutive equal digits (this one).
   * Count numbers with digit sum divisible by K.
   * Count numbers with no digit 7.
   * Count numbers with non-decreasing digits.

2. **Always reduce the problem to:**

   $$
   \text{Answer} = F(b) - F(a-1)
   $$

   That’s the universal trick for ranges.

3. **Recognize the signs fast**:

   * Constraint ≤ 10^18 or 10^100 (too big to brute force).
   * “Count numbers with property …”
   * Property described in terms of digits.

4. **Carry a template in your head** (like your go-to DFS with memo).
   Then, during OA, just adjust the `prevState` logic.

---

## 🔹 Time Breakdown for 20 minutes

In practice, once you know the skeleton:

* 2–3 min: recognize digit DP & define state.
* 10 min: write the standard DFS with memo.
* 5–7 min: adapt condition to the specific problem (like “adjacent not equal”).
* Debug small case quickly (e.g., a=101, b=123).

That’s doable in OA time if you’ve practiced.

---

✅ Rule of thumb:
**If the input is a range \[a,b] with b up to 10^18 and the condition is “digit-based,” it’s digit DP.**

---

Do you want me to draft a **cheat sheet of 3–4 digit DP skeletons** (adjacent-different, digit sum, forbidden digit, monotone digits) so you can “pattern match” instantly in an OA?


---

Perfect 👌 — here’s a **Digit DP Cheat Sheet** that you can literally memorize and reuse in Online Assessments.
Think of it like your “5 skeletons” for DP.

---

# 🧾 Digit DP Cheat Sheet

General formula for range problems:

$$
\text{Answer}(a,b) = F(b) - F(a-1)
$$

where `F(x)` counts valid numbers ≤ x.

---

## 🔹 Skeleton State

```python
def dfs(pos, prevState, tight, leading):
    if pos == n: return valid/end condition
    if memo[pos][prevState][tight][leading] != -1:
        return memo[pos][prevState][tight][leading]

    limit = digits[pos] if tight else 9
    res = 0
    for d in range(0, limit+1):
        if condition fails: continue
        newTight = tight and (d == limit)
        newLeading = leading and (d == 0)
        res += dfs(nextPos, newPrevState, newTight, newLeading)

    memo[pos][prevState][tight][leading] = res
    return res
```

Where:

* `pos`: index of digit in number string (0..n-1).
* `prevState`: property tracker (last digit, sum, etc.).
* `tight`: whether we are still following the upper bound.
* `leading`: whether we are still in leading zeros.

---

## 🔹 Pattern 1: No Adjacent Equal Digits

**Property:** Last digit ≠ current digit.

State:

* `prev` = previous digit (−1 if none).

Condition:

```python
if not leading and d == prev: continue
```

---

## 🔹 Pattern 2: Digit Sum ≤ K

**Property:** Keep track of sum so far.

State:

* `sum` = current sum of digits.

Transition:

```python
newSum = sum + d
if newSum > K: continue
```

---

## 🔹 Pattern 3: Exclude Certain Digits (e.g. no '7')

**Property:** Current digit ≠ forbidden digit.

Condition:

```python
if d == 7: continue
```

---

## 🔹 Pattern 4: Monotone Digits (non-decreasing or strictly increasing)

**Property:** Current digit ≥ previous digit (for non-decreasing).

Condition:

```python
if not leading and d < prev: continue
```

or for strictly increasing:

```python
if not leading and d <= prev: continue
```

---

## 🔹 Pattern 5 (Extra): Count Numbers with Specific Digit

**Property:** Track a boolean flag whether digit appeared.

State:

* `found` = 0/1 flag.

Transition:

```python
newFound = found or (d == targetDigit)
```

At base case:

```python
return 1 if found else 0
```

---

## 🔹 Complexity

* DP states: `len × prevState × tight × leading`.
* For 18-digit numbers:

  * `pos` up to 18–19
  * `prev` up to 10
  * `tight × leading` ≤ 4
    → only a few thousand states.

Each state loops ≤10 digits ⇒ O(2000–3000) per query. Super fast.

---

# 🏁 TL;DR for OA Recognition

* **Input is a huge number (10^18).**
* **They ask: “Count numbers with property …”**
* **Property is digit-based.**
  👉 It’s Digit DP. Use skeleton above, plug in property.

---

⚡ Would you like me to also make a **mini table** mapping “Problem statement → which skeleton to use → which extra state variable to add”? That would let you *pattern match in <10s*.
