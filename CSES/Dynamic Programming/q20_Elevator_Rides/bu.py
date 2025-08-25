n, lt = map(int, input().split())
wt = list(map(int, input().split()))

dp = [[1e9, 1e9] for _ in range(0, 1 << n)]

# Base case: empty subset
dp[0] = [1, 0]

for subset in range(1, 1 << n):
    # rides till now, last occupant last ride weight
    # r, lowt = dp[subset]

    # ltb = last_take_bit
    for ltb in range(n):
        ltb_mask = 1 << ltb
        # if bit is set, try it as last
        if subset & ltb_mask:
            # eetl_mask = every elem/person except ltb-th mask
            eetl_mask = subset ^ ltb_mask
            curr_ss = dp[eetl_mask]
            cr, clowt = curr_ss
            if clowt + wt[ltb] <= lt:
                # allow current(last) ride, occupany increses
                last_taken = [cr, clowt + wt[ltb]]
                if dp[subset][0] > last_taken[0]:
                    dp[subset] = last_taken
                elif dp[subset][0] == last_taken[0] and dp[subset][1] > last_taken[1]:
                    dp[subset] = last_taken
            else:
                # new ride
                last_taken = [cr + 1, wt[ltb]]
                if dp[subset][0] > last_taken[0]:
                    dp[subset] = last_taken
                elif dp[subset][0] == last_taken[0] and dp[subset][1] > last_taken[1]:
                    dp[subset] = last_taken


print(dp[(1 << n) - 1][0])

# ABove gives tle due to many if statements
# check python_optimized version

"""
# Also correct, because Python compares tuples/lists lexicographically.
n, lt = map(int, input().split())
wt = list(map(int, input().split()))

dp = [[1e9, 1e9] for _ in range(1 << n)]

# Base case: no people => 0 rides, 0 weight
dp[0] = [0, 0]

for subset in range(1, 1 << n):
    for ltb in range(n):
        if subset & (1 << ltb):  # person ltb included
            prev = subset ^ (1 << ltb)
            rides, last_wt = dp[prev]

            if last_wt + wt[ltb] <= lt:
                candidate = [rides, last_wt + wt[ltb]]
            else:
                candidate = [rides + 1, wt[ltb]]

            dp[subset] = min(dp[subset], candidate)

# answer: number of rides needed for all people
print(dp[(1 << n) - 1][0])

"""
