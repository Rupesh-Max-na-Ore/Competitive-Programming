def solve(k):
    digit_length = 1
    count = 9
    start = 1
    # print(digit_length,count,start)
    # Step 1: Figure out which digit length block contains the kth digit
    while k > digit_length * count:
        k -= digit_length * count
        digit_length += 1
        count *= 10
        start *= 10
    # print(digit_length,count,start,k)
    # Step 2: Find the actual number containing the kth digit
    number_index = (k-1) // digit_length
    digit_index = (k-1) % digit_length
    
    number = start + number_index
    # print(number_index,digit_index-1,number)
    return str(number)[digit_index]

t = int(input())
for _ in range(t):
    k = int(input())
    print(solve(k))
