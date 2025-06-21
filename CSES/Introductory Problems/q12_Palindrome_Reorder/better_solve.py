from collections import Counter
#Pythonic, but few tcs are coming wrong - TC 9 and TC 15
"""
Test 15

Verdict: WRONG ANSWER
input
AADDDCC

correct output
ACDDDCA

user output
ACDDDDDCA
"""
def make_palindrome(s):
    count = Counter(s)
    odd_chars = [ch for ch in count if count[ch] % 2 != 0]

    if len(odd_chars) > 1:
        return "NO SOLUTION"

    half = []
    middle = ''
    
    for ch in sorted(count.keys()):  # sort for consistent output (optional)
        times = count[ch] // 2
        half.append(ch * times)
        if count[ch] % 2 == 1:
            middle = ch * count[ch]

    first_half = ''.join(half)
    return first_half + middle + first_half[::-1]

# # Input
# s = input()
# print(make_palindrome(s))

# from collections import Counter

# def make_palindrome(s):
#     count = Counter(s)
#     odd_chars = [ch for ch in count if count[ch] % 2 != 0]

#     if len(odd_chars) > 1:
#         return "NO SOLUTION"

#     half = []
#     middle = ''
    
#     for ch in sorted(count.keys()):  # optional sorting for consistent output
#         times = count[ch] // 2
#         half.append(ch * times)
#         if count[ch] % 2 == 1:
#             middle = ch  # just ONE odd character placed in middle

#     first_half = ''.join(half)
#     return first_half + middle + first_half[::-1]

# # Input
# s = input()
# print(make_palindrome(s))
