def sets(n):
    total = n * (n + 1) // 2
    if total % 2 == 1:
        return "NO"

    first_set, second_set = [], []
    l = 1
    r = n - 1 if n % 2 == 1 else n
    run = 1

    while l < r:
        if run % 2 == 1:
            first_set.extend([l, r])
        else:
            second_set.extend([l, r])
        l += 1
        r -= 1
        run += 1

    if n % 2 == 1:
        second_set.append(n)

    return "YES", first_set, second_set


# Main I/O logic
n = int(input())
result = sets(n)

if result == "NO":
    print("NO")
else:
    print("YES")
    first, second = result[1], result[2]
    print(len(first))
    print(' '.join(map(str, first)))
    print(len(second))
    print(' '.join(map(str, second)))
