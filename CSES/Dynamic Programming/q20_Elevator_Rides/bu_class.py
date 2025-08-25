from typing import List


class ElevatorRides:
    def __init__(self, weights: List[int], max_weight: int):
        self.n = len(weights)
        self.weights = weights
        self.max_weight = max_weight
        self.dp = [(self.n + 1, 0)] * (1 << self.n)  # (rides, current_weight)

    def solve(self) -> int:
        # base case: empty set requires 1 ride with 0 weight
        self.dp[0] = (1, 0)

        for mask in range(1 << self.n):
            rides, cur_weight = self.dp[mask]
            for i in range(self.n):
                if not (mask & (1 << i)):  # person i not in mask yet
                    next_mask = mask | (1 << i)
                    w = self.weights[i]

                    if cur_weight + w <= self.max_weight:
                        option = (rides, cur_weight + w)
                    else:
                        option = (rides + 1, w)

                    # take lexicographically smaller (min rides, then min weight)
                    if option < self.dp[next_mask]:
                        self.dp[next_mask] = option

        full_mask = (1 << self.n) - 1
        return self.dp[full_mask][0]


weights = [10, 10, 9, 8, 7, 5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2]
maxwt = 10
solver = ElevatorRides(weights, maxwt)
print(solver.solve())  # Output: 10
