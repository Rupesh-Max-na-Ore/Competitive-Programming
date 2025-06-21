def nit(n):
    results = []
    for k in range(1, n + 1):
        total_positions = k * k * (k * k - 1) // 2
        attacking_positions = 0
        if k > 2:
            attacking_positions = 4 * (k - 1) * (k - 2)
        results.append(total_positions - attacking_positions)
    return results


n = int(input())
ans = nit(n)
for val in ans:
    print(val)