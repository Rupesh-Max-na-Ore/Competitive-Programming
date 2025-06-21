def beaut(n, a):
    if n==1:
        a[0] = 1
        return True
    elif n == 2 or n == 3:
        return False
    else:
        # if n % 2 ==1 :
        #     one_pos = n // 2
        #     a[one_pos] = 1
        #     for i in range(n // 2):
        #         even = (i+1)*2
        #         a[i] = even
        #         a[i+one_pos+1] = even +1
        # else:
        #     for i in range(n // 2):
        #         one_pos = n // 2
        #         even = (i+1)*2
        #         a[i] = even
        #         a[i+one_pos] = even - 1
        # return True
        # #above is same as below
        is_odd = False
        if n % 2 ==1 :
            is_odd = True
        one_pos = n // 2
        if(is_odd):
            a[one_pos] = 1
        for i in range(n // 2):
            even = (i+1)*2
            a[i] = even
            a[i+one_pos+ (1 if (is_odd) else 0)] = even + (1 if (is_odd) else -1)
        return True


n = int(input())
a = [0] * n
if beaut(n, a):
    print(*a)
else:
    print("NO SOLUTION")

"""
#pythonic way
n = int(input())

if n == 1:
    print(1)
elif n == 2 or n == 3:
    print("NO SOLUTION")
else:
    even = [i for i in range(2, n + 1, 2)]
    odd = [i for i in range(1, n + 1, 2)]
    print(*even, *odd)
"""