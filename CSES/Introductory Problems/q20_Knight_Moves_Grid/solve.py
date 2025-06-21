"""
Knight Moves Grid

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Knight Moves Grid




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



There is a knight on an n \times n chessboard. For each square, print the minimum number of moves the knight needs to do to reach the top-left corner.
Input
The only line has an integer n.
Output
Print the number of moves for each square.
Constraints

4 \le n \le 1000

Example
Input:
8

Output:
0 3 2 3 2 3 4 5 
3 4 1 2 3 4 3 4 
2 1 4 3 2 3 4 5 
3 2 3 2 3 4 3 4 
2 3 2 3 4 3 4 5 
3 4 3 4 3 4 5 4 
4 3 4 3 4 5 4 5 
5 4 5 4 5 4 5 6 
"""

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
