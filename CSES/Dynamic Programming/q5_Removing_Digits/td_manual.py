import sys
sys.setrecursionlimit(10**7)

# dp[i] will store the minimum steps to reduce i to 0
def fn(num, dp):
    if num == 0:
        # If the number is already 0, no steps are needed
        return 0
    if num < 0:
        # return a big no. to ensure it is not counted as min_step update
        return 10**7
    if dp[num] != -1 :
        return dp[num]
    
    
    steps = 0
    min_steps = 10**7 #large no. init
    # extract all digits of num variable and store them in a list
    digits = [int(d) for d in str(num)]
    # for each digit
    for digit in digits:
        if digit == 0: #skip 0s
            continue
        # count step as 1, and recursively call num - digit steps
        steps = 1 + fn(num - digit, dp)
        min_steps = min(min_steps, steps)
    dp[num] = min_steps
    return min_steps
    

num = int(input())
res = fn(num, [-1 for _ in range(num+1)])
print(res)