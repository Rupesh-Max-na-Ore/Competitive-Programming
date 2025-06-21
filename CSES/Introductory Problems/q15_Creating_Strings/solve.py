"""
Creating Strings

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Creating Strings




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



Given a string, your task is to generate all different strings that can be created using its characters.
Input
The only input line has a string of length n. Each character is between a–z.
Output
First print an integer k: the number of strings. Then print k lines: the strings in alphabetical order.
Constraints

1 \le n \le 8

Example
Input:
aabac

Output:
20
aaabc
aaacb
aabac
aabca
aacab
aacba
abaac
abaca
abcaa
acaab
acaba
acbaa
baaac
baaca
bacaa
bcaaa
caaab
caaba
cabaa
cbaaa
    
    
Introductory Problems...
Palindrome ReorderGray CodeTower of HanoiCreating StringsApple DivisionChessboard and QueensRaab Game IMex Grid Construction...
    Your submissions

"""

# prev_ch is useless - initially thot it might help mitigate duplicates w/o a set, but ig not

def perm(s, i, n, prev_ch, hf, words):
    if(i==n):
        words.add(s)
    else:
        for ch in hf:
            if hf[ch]!=0:
                if prev_ch == ch:
                    hf[ch]-=1
                    new_s = s+ch
                    perm(new_s, i+1, n, ch, hf, words)
                    hf[ch]+=1
                else:
                    hf[ch]-=1
                    new_s = s+ch
                    perm(new_s, i+1, n, ch, hf, words)
                    hf[ch]+=1



def solve(str):
    n = len(str)
    chs = [ch for ch in str]
    # print(chs)
    hf = {}
    for ch in chs:
        if ch in hf:
            hf[ch]+=1
        else:
            hf[ch]=1
    # print(hf)
    words = set()
    perm("", 0, n, '', hf, words)
    # print(words)
    print(len(words))
    word_list = sorted(words)
    for word in word_list:
        print(word)

str = input()
solve(str)