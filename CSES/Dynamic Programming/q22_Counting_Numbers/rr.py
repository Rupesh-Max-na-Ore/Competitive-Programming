from functools import lru_cache


def count_valid(x: int) -> int:
    if x < 0:
        return 0
    digits = list(map(int, str(x)))
    n = len(digits)

    @lru_cache(None)
    def dp(pos: int, prev: int, tight: bool, leading: bool) -> int:
        if pos == n:
            return 0 if leading else 1  # valid if number formed

        limit = digits[pos] if tight else 9
        total = 0

        for d in range(0, limit + 1):
            if not leading and d == prev:
                continue
            new_leading = leading and (d == 0)
            new_prev = -1 if new_leading else d
            total += dp(
                pos + 1,
                new_prev,
                tight and d == limit,
                new_leading,
            )
        return total

    return dp(0, -1, True, True)


a, b = map(int, input().split())
if a - 1 == 0:
    print(count_valid(b) - 0)
elif a == 0:
    print(count_valid(b) + 1)
else:
    print(count_valid(b) - (count_valid(a - 1)))
