def can_empty(a, b):
    total = a + b
    if total % 3 != 0:
        return "NO"
    if min(a, b) * 2 < max(a, b):
        return "NO"
    return "YES"

def solve():
    t = int(input())
    results = []
    for _ in range(t):
        a, b = map(int, input().split())
        results.append(can_empty(a, b))
    print('\n'.join(results))

# Run the fn
solve()


