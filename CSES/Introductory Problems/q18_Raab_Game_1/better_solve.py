#TC O[n] greedy construction
def solve(n,a,b):
    if(n < a+b):
        print("NO")
        return
    elif((a+b)>0 and (a==0 or b==0)):
        print("NO")
        return
    
    # else:
    print("YES")
    # first player arragd.
    draws = n - (a+b)
    sz = n - draws # a+b
    # max part of 1st player wins = a = sz - b
    for i in range(b+1,sz+1,1):
        print(i, end = " ")
    # min part of 1st player for 2nd player wins = b 
    for i in range(1,b+1,1):
        print(i, end = " ")
    #draws part from end = n - sz
    for i in range(sz+1,n+1,1):
        print(i, end = " ")    
    print()
    # second player as is = 1 to n
    for i in range(1,n+1,1):
        print(i, end = " ")
    print()

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    solve(n, a, b)
