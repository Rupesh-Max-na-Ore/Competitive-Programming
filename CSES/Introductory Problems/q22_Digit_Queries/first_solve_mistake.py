"""
Digit Queries

Task
Submit
Results
Statistics
Tests

    
    
  

  

    
CSES - Digit Queries




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



Consider an infinite string that consists of all positive integers in increasing order:
12345678910111213141516171819202122232425...
Your task is to process q queries of the form: what is the digit at position k in the string?
Input
The first input line has an integer q: the number of queries.
After this, there are q lines that describe the queries. Each line has an integer k: a 1-indexed position in the string.
Output
For each query, print the corresponding digit.
Constraints

1 \le q \le 1000
1 \le k \le 10^{18}

Example
Input:
3
7
19
12

Output:
7
4
1


"""
# import math
# def solve(n):
#     d = num_digits = math.floor(math.log10(n)) + 1
#     print(d)
#     r, pow, allnine = n,1,0
#     for i in range(1,num_digits):
#         if r - 9*i*pow >0:
#             r-= 9*i*pow
#         else:
#             break
#         pow*=10
#         allnine = allnine*10+9
#     print(r, pow, allnine)
#     l=r//num_digits
    
#     rem = r%num_digits
#     no = allnine + l

#     print(l,rem,no)
#     if rem == 0:
#         pow*=10
#         numbr = str(no)
#         print(numbr)
#         # return (str(no%pow))
#         return numbr[len(numbr)-1]
#     else:
#         no+=1
#         numbr = str(no)
#         print(numbr)
#         return (numbr[rem-1])

# # i/p handling
# t = int(input())
# for _ in range(t):
#     c = int(input())
#     print(solve(c))

import math
def solve(n):
    d = num_digits = 0
    print(d)
    r, pow, allnine,i = n,1,0,1
    print(r, pow, allnine,i,d)
    while r - 9*i*pow >0:
        r-= 9*i*pow
        d+=1
        i+=1
        pow*=10
        allnine = allnine*10+9
    print(r, pow, allnine,i,d)
    num_digits=i #d
    l=r//num_digits
    
    rem = r%num_digits
    no = allnine + l

    print(l,rem,no)
    if rem == 0:
        pow*=10
        numbr = str(no)
        print(numbr)
        # return (str(no%pow))
        return numbr[len(numbr)-1]
    else:
        no+=1
        numbr = str(no)
        print(numbr)
        return (numbr[rem-1])

# i/p handling
t = int(input())
for _ in range(t):
    c = int(input())
    print(solve(c))