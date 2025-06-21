# 

# above is wrong cuz order
# actual move(a,b) - need to compare top of a and b, and put smaller to other
# so stack seems obvious, but array/list does the job too 
def move_disk(from_peg, to_peg, from_label, to_label):
    if not from_peg:
        disk = to_peg.pop()
        from_peg.append(disk)
        print(f"{to_label} {from_label}")
    elif not to_peg:
        disk = from_peg.pop()
        to_peg.append(disk)
        print(f"{from_label} {to_label}")
    elif from_peg[-1] > to_peg[-1]:
        disk = to_peg.pop()
        from_peg.append(disk)
        print(f"{to_label} {from_label}")
    else:
        disk = from_peg.pop()
        to_peg.append(disk)
        print(f"{from_label} {to_label}")

def iterative_tower_of_hanoi(n):
    total_moves = 2**n - 1
    src = list(range(n, 0, -1))
    aux = []
    dst = []

    if n % 2 == 0:
        aux_label, dst_label = 3, 2
    else:
        aux_label, dst_label = 2, 3

    print(total_moves)
    for i in range(1, total_moves + 1):
        if i % 3 == 1:
            move_disk(src, dst, 1, dst_label)
        elif i % 3 == 2:
            move_disk(src, aux, 1, aux_label)
        else:
            move_disk(aux, dst, aux_label, dst_label)

# Example:
n = int(input())
iterative_tower_of_hanoi(n)