def Weird_Algo(n):
    if n <= 0: 
        return "Wrong input"
    
    print(n, end=" ")
    while n != 1:
        if n % 2 == 1: 
            n = n * 3 + 1
        else: 
            n = n // 2
        print(n, end=" ")

n = int(input())
Weird_Algo(n) 