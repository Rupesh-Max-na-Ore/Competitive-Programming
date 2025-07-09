def slv(n, sum, curr):
    if sum < 0 :
        return 0
    if sum == 0 :
        return 1
    
    ways = 0
    for coin in curr :
        ways += slv(n, sum - coin, curr)
    
    return ways

n, sum = map(int, input().split())
curr = list(map(int, input().split()))
print(slv(n, sum, curr))