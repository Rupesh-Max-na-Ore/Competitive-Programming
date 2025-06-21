from collections import Counter

def solve(s):
    n = len(s)
    freq = Counter(s)

    # Early check: impossible if any char occurs too frequently
    if any(count > (n + 1) // 2 for count in freq.values()):
        return "-1"

    result = []
    prev_char = ''

    for _ in range(n):
        found = False
        # Try characters in lex order
        for ch in sorted(freq.keys()):
            if ch == prev_char:
                continue  # can't place same as previous
            freq[ch] -= 1
            # Check if placing ch here leads to dead end later
            if all(c <= (n - len(result) - 1 + 1) // 2 for c in freq.values()):
                result.append(ch)
                prev_char = ch
                found = True
                if freq[ch] == 0:
                    del freq[ch]
                break
            freq[ch] += 1  # rollback if it doesn't work
        if not found:
            return "-1"

    return ''.join(result)

s = input().strip()
print(solve(s))
#tle large tcs