def solve():
    s = input()
    chl = list(s)
    hmf = {}
    for ch in chl:
        if ch in hmf:
            hmf[ch]+=1
        else:
            hmf[ch]=1
    oddchar=''
    odds = 0
    odd_ch_freq = 0
    for ch in hmf:
        if hmf[ch] % 2 == 1:
            odds+=1
            oddchar = ch
            odd_ch_freq = hmf[ch]
            if(odds >= 2):
                print("NO SOLUTION")
                #break
                return
    fst =[]
    mid= oddchar * odd_ch_freq
    if odds == 1:
        hmf.pop(oddchar)
    for ch in hmf:
        times = hmf[ch]//2
        fst.append(ch * times)

    first = ''.join(fst)
    print(first + mid + first[::-1]) 

solve()