

def solve(n):
    a = [-1] *(n+1)
    a[0] = 0
    a[1] = 1
    a[2] = 2
    a[3] = 4
    pick =0
    notpick=0
    for i in range (1,7):
        pick += dice(n-i,a)
        # notpick += dice(n,a)
    
    # return pick + notpick
    a[n] = pick + notpick

    return a[n]

def dice(n,a):
    if n==0:
        return 1
    if a[n] != -1:
        return a[n]
    pick =0
    notpick=0
    for i in range (1,7):
        pick += dice(n-i,a)
        # notpick += dice(n,a)
    
    a[n] = pick + notpick

    return a[n]

n = int(input())

print(solve(n))