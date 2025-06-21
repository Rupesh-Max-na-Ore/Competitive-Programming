"""
Palindrome Reorder

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Palindrome Reorder




addEventListener("DOMContentLoaded", function (e) {
    const mathElements = document.getElementsByClassName("math");
    const macros = {};
    for (let element of mathElements) {
        katex.render(element.textContent, element, {
            displayMode: element.classList.contains("math-display"),
            throwOnError: false,
            globalGroup: true,
            macros,
        });
    }
});


Time limit: 1.00 s
Memory limit: 512 MB



Given a string, your task is to reorder its letters in such a way that it becomes a palindrome (i.e., it reads the same forwards and backwards).
Input
The only input line has a string of length n consisting of characters A–Z.
Output
Print a palindrome consisting of the characters of the original string. You may print any valid solution. If there are no solutions, print "NO SOLUTION".
Constraints

1 \le n \le 10^6

Example
Input:
AAAACACBA

Output:
AACABACAA
"""

s = input()
chl = list(s)
hmf = {}
for ch in chl:
    if ch in hmf:
        hmf[ch]+=1
    else:
        hmf[ch]=1
odds = 0
oddchar = ''
stri = []
mid = 0
for ch in hmf:
    if hmf[ch] % 2 == 1:
        odds+=1
        oddchar = ch
        odd_ch_freq = hmf[ch]
        if(odds >= 2):
            print("NO SOLUTION")
            break
mid = 0
if odds <=1 :
    for ch in hmf:
        if hmf[ch] % 2 == 0:
            f = hmf[ch]
            for _ in range(f):
                stri.insert(mid,ch)
                if (_ % 2 == 1):
                    mid+=1
            #hmf.pop(ch)
if odds <=1 :
    if oddchar != '':
        for _ in range(odd_ch_freq):
            stri.insert(mid,oddchar)
    st = ''.join(map(str, stri))
    print(st)
