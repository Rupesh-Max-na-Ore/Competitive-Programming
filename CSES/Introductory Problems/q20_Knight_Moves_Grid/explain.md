This is a **Breadth-First Search (BFS)** problem on a 2D grid involving knight moves (like in chess).

---

## 🔍 **Problem Overview**

* You're given an `n x n` chessboard.
* A **knight** starts at the **top-left corner** (cell `(0, 0)`).
* For **each square on the board**, you must compute and print the **minimum number of knight moves** required to reach `(0, 0)` from that square.

---

## 📚 **Understanding the Knight’s Moves**

A knight moves in **L-shapes**:

* 2 steps in one direction and 1 step perpendicular.

Possible 8 directions:

```python
(+2, +1), (+1, +2), (-1, +2), (-2, +1),
(-2, -1), (-1, -2), (+1, -2), (+2, -1)
```

---

## 🧠 **Key Idea**

We need to compute the shortest distance **from every cell to (0, 0)** — which is symmetric to computing **from (0, 0) to every cell**.

So:

* We do a **BFS from (0, 0)**.
* BFS is ideal because all edges (moves) cost the same → shortest path in unweighted graphs.

---

## ✅ **Steps**

1. Initialize an `n x n` grid `dist` with -1 (unvisited).
2. Set `dist[0][0] = 0`.
3. Use a **queue** to perform BFS.
4. For each current cell, try all 8 knight moves.
5. If a move leads to a valid, unvisited cell — mark its distance and enqueue it.
6. After BFS, print the grid.

---

## 🧑‍💻 Python Code

```python
from collections import deque

def knight_moves_grid(n):
    # 8 possible knight moves
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    
    # Distance grid initialized to -1
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    
    # BFS queue starting from (0, 0)
    queue = deque()
    queue.append((0, 0))
    dist[0][0] = 0  # Starting point has distance 0
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            
            # Check if move is within bounds and unvisited
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    
    # Print the result
    for row in dist:
        print(" ".join(map(str, row)))

# Example usage:
n = int(input())
knight_moves_grid(n)
```

---

## 🧪 Example Output (for `n = 8`)

```
0 3 2 3 2 3 4 5
3 4 1 2 3 4 3 4
2 1 4 3 2 3 4 5
3 2 3 2 3 4 3 4
2 3 2 3 4 3 4 5
3 4 3 4 3 4 5 4
4 3 4 3 4 5 4 5
5 4 5 4 5 4 5 6
```

---

## 🧠 Why BFS Works

* Each knight move takes equal effort (1 move).
* BFS explores all nodes at distance `d` before distance `d+1`.
* So the first time you reach a square, it’s always via the shortest path.

---

Would you like this explained with diagrams or step-by-step visual BFS for a small grid like `4x4`?
