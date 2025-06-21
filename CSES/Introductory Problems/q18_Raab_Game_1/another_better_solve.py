# def rotate_sublist(lst, start, end, k):
#     sublist = lst[start:end+1]
#     n = len(sublist)
#     k = k % n  # to handle rotations > length
#     rotated = sublist[-k:] + sublist[:-k]
#     return lst[:start] + rotated + lst[end+1:]

def solve(n,a,b):
    if(n -(a+b) < 0):
        print("No")
        return
    elif((a+b)>0 and (a==0 or b==0)):
        print("NO")
        return
    
    f = [i for i in range(1,n+1,1)]
    draws = n - (a+b)
    rotated = [j for j in range (a+1, a+b+1, 1)]+[i for i in range (1,a+1,1)]
    s = rotated + [k for k in range (a+b+1, n+1, 1)]
    print("YES")
    print(" ".join(map(str,f)))
    print(" ".join(map(str,s)))


t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    solve(n, a, b)
