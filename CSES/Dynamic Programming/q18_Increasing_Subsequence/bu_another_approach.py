n = int(input())
arr = list(map(int, input().split()))

import bisect


def length_of_LIS(arr):
    piles = []

    for x in arr:
        i = bisect.bisect_left(piles, x)
        if i == len(piles):
            piles.append(x)  # New pile
        else:
            piles[i] = x  # Replace top of an existing pile

    return len(piles)


print(length_of_LIS(arr))

# For java code Treeset will be shortest to write
# For python and cpp Binary search library is shorter

# st = []
# maxsz = 0

# for a in arr:
#     if len(st) == 0:
#         st.append(a)
#     elif st[len(st) - 1] >= a:
#         while len(st) > 0 and st[len(st) - 1] >= a:
#             st.pop()
#         st.append(a)
#     else:
#         st.append(a)
#     maxsz = max(maxsz, len(st))

# print(maxsz)
