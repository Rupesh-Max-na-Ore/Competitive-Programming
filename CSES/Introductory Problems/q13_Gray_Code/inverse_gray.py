g = int(input())
#inverse graycode
n=0
li = g
while li != 0:
    li /=2
    n+=1
nbit = g >> n-1
construct_n = nbit
for i in range(n-2, -1, -1):
    gbit = 1 if (g & (1 << i)!=0) else 0
    nbit = nbit ^ gbit
    construct_n = (construct_n << 1)|nbit
print(construct_n) 

##smaller code to do same
# g = int(input())

# n = g
# while g > 0:
#     g = g >> 1
#     n = n ^ g

# print(n)
