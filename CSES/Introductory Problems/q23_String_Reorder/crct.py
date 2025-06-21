import heapq
from collections import Counter

def solve(s):
    n = len(s)
    freq = Counter(s)

    # Step 1: Feasibility check
    if any(count > (n + 1) // 2 for count in freq.values()):
        return "-1"

    # Step 2: Max-heap based on frequency and lex order
    heap = [(-cnt, ch) for ch, cnt in sorted(freq.items())]  # sort for lex order
    heapq.heapify(heap)

    result = []
    prev_freq, prev_char = 0, ''

    while heap:
        freq, ch = heapq.heappop(heap)

        result.append(ch)

        # Push back the previous character if it still has freq
        if prev_freq < 0:
            heapq.heappush(heap, (prev_freq, prev_char))

        # Decrease freq of current char
        prev_freq, prev_char = freq + 1, ch

    return ''.join(result)

s = input().strip()
print(solve(s))