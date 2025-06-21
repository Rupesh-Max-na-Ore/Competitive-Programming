def missing(n : int, a : list[int]):
    lis = [False] * n
    for i in range(len(a)):
        lis[a[i]-1] = True

    for i in range(n):
        if(lis[i]==False):
            print(i+1)
            return
  
#n, a = int(input()), list(input())
#missing(n, a)
n = int(input())
a = list(map(int, input().split()))

missing(n, a)