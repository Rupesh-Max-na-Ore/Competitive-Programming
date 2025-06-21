from typing import List

def missing(n: int, a: List[int]):
    lis = [False] * n
    for num in a:
        lis[num - 1] = True

    for i in range(n):
        if not lis[i]:
            print(i + 1)
            return

n = int(input())
a = list(map(int, input().split()))
missing(n, a)

# def missing2(n, a):
#     lis = [False] * n
#     for num in a:
#         lis[num - 1] = True

#     for i in range(n):
#         if not lis[i]:
#             print(i + 1)
#             return

# n = int(input())
# a = list(map(int, input().split()))
# missing2(n, a)
