from collections import Counter

def solve(s):
    n = len(s)
    freq = Counter(s)

    # Early impossible check
    if any(freq[c] > (n + 1) // 2 for c in freq):
        return "-1"

    res = []
    prev = None

    for _ in range(n):
        for ch in sorted(freq.keys()):
            if ch == prev:
                continue

            # Try placing ch
            freq[ch] -= 1
            remaining_max = max(freq.values(), default=0)

            # Check if rest of string can be completed
            if remaining_max <= (n - len(res) - 1 + 1) // 2:
                res.append(ch)
                if freq[ch] == 0:
                    del freq[ch]
                prev = ch
                break
            else:
                # Roll back and try next char
                freq[ch] += 1
        else:
            # No valid character could be placed
            return "-1"

    return ''.join(res)
s = input().strip()
print(solve(s))