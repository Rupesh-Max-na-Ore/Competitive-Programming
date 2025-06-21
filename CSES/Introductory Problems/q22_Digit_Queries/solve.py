def solve(n):
    d = num_digits = 0
    # print(d)
    r, pow, allnine,i = n,1,0,1
    # print(r, pow, allnine,i,d)
    while r - 9*i*pow >0:
        r-= 9*i*pow
        d+=1
        i+=1
        pow*=10
        allnine = allnine*10+9
    # print(r, pow, allnine,i,d)
    num_digits=i #d
    l=r//num_digits
    
    rem = r%num_digits
    no = allnine + l

    # print(l,rem,no)
    if rem == 0:
        pow*=10
        numbr = str(no)
        # print(numbr)
        # return (str(no%pow))
        return numbr[len(numbr)-1]
    else:
        no+=1
        numbr = str(no)
        # print(numbr)
        return (numbr[rem-1])

# i/p handling
t = int(input())
for _ in range(t):
    c = int(input())
    print(solve(c))