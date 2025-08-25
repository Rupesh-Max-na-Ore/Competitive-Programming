def greedy_elevator_rides(weights, max_wt):
    # Sort descending
    weights.sort(reverse=True)
    print(weights)
    rides = 0

    while weights:
        cap = max_wt
        i = 0
        while i < len(weights):
            if weights[i] <= cap:
                cap -= weights[i]
                weights.pop(i)  # remove person
            else:
                i += 1
        rides += 1
    return rides


# # Example
# n, x = 4, 10
# weights = [4, 8, 6, 1]
# print(greedy_elevator_rides(weights, x))  # Might give wrong answer for some inputs

n, maxwt = map(int, input().split())
wts = list(map(int, input().split()))

print(greedy_elevator_rides(wts, maxwt))
