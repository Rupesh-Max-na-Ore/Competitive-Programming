Great! For tighter constraints (like larger `n`, or many test cases `t`), the recursive **backtracking** approach is too slow.

Here’s a **faster and more practical strategy** for the *Raab Game I* problem:

---

## ✅ Problem Recap:

* Two players each have cards `1` to `n`.
* They play all cards once, getting 1 point for the higher card in a round.
* You are given:

  * `n`: total cards per player
  * `a`: final score of player A
  * `b`: final score of player B
* You must output a valid sequence of plays (any one) or "NO".

---

## ⚡ Efficient Greedy Strategy:

Let’s fix player A’s sequence as `[1, 2, ..., n]`, and construct player B’s sequence in a way that gives exactly `b` wins to player B and `a` wins to player A.

---

### 💡 Idea:

* Sort Player A’s cards: `A = [1, 2, ..., n]`
* Sort Player B’s cards: `B = [1, 2, ..., n]`
* To control who wins:

  * To make **Player A win**, assign Player B a smaller card than A’s current.
  * To make **Player B win**, assign Player B a larger card than A’s current.
  * To make a **tie**, assign equal cards.

We’ll greedily assign cards to B while counting victories to match `a` and `b`.

---

### ✅ Code:

```python
def solve(n, a, b):
    if a + b > n:
        print("NO")
        return

    A = list(range(1, n + 1))          # Player A fixed order
    B = [0] * n                        # We'll construct B's order
    used = [False] * (n + 1)

    # Step 1: Let B win exactly `b` times by assigning bigger cards
    ai = n - 1
    bi = n
    for i in range(n - 1, -1, -1):
        if b > 0:
            while bi > 0 and (used[bi] or bi <= A[i]):
                bi -= 1
            if bi == 0:
                print("NO")
                return
            B[i] = bi
            used[bi] = True
            b -= 1

    # Step 2: Let A win exactly `a` times by assigning smaller cards
    bi = 1
    for i in range(n):
        if B[i] == 0 and a > 0:
            while bi <= n and (used[bi] or bi >= A[i]):
                bi += 1
            if bi > n:
                print("NO")
                return
            B[i] = bi
            used[bi] = True
            a -= 1

    # Step 3: Assign equal cards to tie the rest
    for i in range(n):
        if B[i] == 0:
            for x in range(1, n + 1):
                if not used[x] and x == A[i]:
                    B[i] = x
                    used[x] = True
                    break
            if B[i] == 0:
                # Try assigning any unused card
                for x in range(1, n + 1):
                    if not used[x]:
                        B[i] = x
                        used[x] = True
                        break

    if any(x == 0 for x in B):
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, A)))
        print(" ".join(map(str, B)))
```

---

### 🧪 Example Usage:

```python
t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    solve(n, a, b)
```

---

### 🔍 Time Complexity:

* **O(n log n)** worst-case (mostly O(n) due to greedy construction)
* Handles up to **t = 1000** and **n = 100** easily

---

Would you like me to explain how to extend this to generate **multiple different valid outcomes**, or just the fastest one?
