import sys

sys.setrecursionlimit(10**7)

n = int(input())
total = n * (n + 1) // 2

if total % 2 != 0:
    print(0)
    exit()

target = total // 2
memo = {}


def count_subsets(i, curr_sum):
    if curr_sum > target:
        return 0
    if i > n:
        return 1 if curr_sum == target else 0
    if (i, curr_sum) in memo:
        return memo[(i, curr_sum)]

    # Option 1: include i in the subset
    take = count_subsets(i + 1, curr_sum + i)
    # Option 2: exclude i from the subset
    leave = count_subsets(i + 1, curr_sum)

    memo[(i, curr_sum)] = take + leave
    return memo[(i, curr_sum)]


ans = count_subsets(1, 0) // 2
print(ans)
