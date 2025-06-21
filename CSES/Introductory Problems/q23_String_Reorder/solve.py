"""
String Reorder

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - String Reorder




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



Your task is to reorder the characters of a string so that no two adjacent characters are the same. What is the lexicographically minimal such string?
Input
The only line has a string of length n consisting of characters A–Z.
Output
Print the lexicographically minimal reordered string where no two adjacent characters are the same. If it is not possible to create such a string, print -1.
Constraints

1 \le n \le 10^6

Example
Input:
HATTIVATTI

Output:
AHATITITVT

"""
# doesn't work for AABBCCC ->stucks at ABABCcC
import string
def solve(s):
    n = len(s)
    hf={}
    for ch in s:
        if ch not in hf:
            hf[ch]=1
        else:
            hf[ch]+=1
    stri=[]
    i=0
    while i<n:
        if i==0:
            for ch in string.ascii_uppercase:
                if ch in hf:
                    stri.append(ch)
                    hf[ch]-=1
                    if hf[ch] == 0:
                        del hf[ch]
                    break
            i+=1
        else:
            prev = stri[i-1]
            haa = False
            for ch in string.ascii_uppercase:
                if ch in hf and ch != prev:
                    haa = True
                    stri.append(ch)
                    hf[ch]-=1
                    if hf[ch] == 0:
                        del hf[ch]
                    break
            i+=1
            if haa == False:
                return "-1"
    return "".join(map(str,stri))
    



s = input().strip()
print(solve(s))