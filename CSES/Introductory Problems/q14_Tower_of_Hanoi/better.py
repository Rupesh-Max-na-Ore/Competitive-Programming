def toh(n, source, auxiliary, target, moves):
    if n == 0:
        return
    toh(n - 1, source, target, auxiliary, moves)
    moves.append((source, target))
    toh(n - 1, auxiliary, source, target, moves)

def solve(n):
    moves = []
    toh(n, 1, 2, 3, moves)
    print(len(moves))
    for move in moves:
        print(move[0], move[1])

n = int(input())
solve(n)
