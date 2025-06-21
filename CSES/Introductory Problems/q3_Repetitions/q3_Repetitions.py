"""
CSES Problem Set
      Repetitions

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Repetitions




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



You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.
Input
The only input line contains a string of n characters.
Output
Print one integer: the length of the longest repetition.
Constraints

1 \le n \le 10^6

Example
Input:
ATTCGGGA

Output:
3
"""

from typing import List

def rep(a:List[str]):
    n = len(a)
    l, r = 0, 1
    maxLen = 1

    while r < n:
        if a[l] == a[r]:
            r += 1
        else:
            maxLen = max(maxLen, r - l)
            l = r
            r += 1

    # Check last repetition after loop ends
    maxLen = max(maxLen, r - l)

    return (maxLen)

lst = list(input())
print(rep(lst))