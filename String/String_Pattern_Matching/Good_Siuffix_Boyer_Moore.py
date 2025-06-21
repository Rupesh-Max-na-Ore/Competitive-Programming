def build_good_suffix_table(pattern):
    m = len(pattern)
    border_pos = [0] * (m + 1)
    shift = [0] * (m + 1)

    print(f"\n[ Step 1: Compute border positions for suffixes ]")
    print(f"{'-'*50}")

    # Step 1: Compute border positions
    i = m
    j = m + 1
    border_pos[i] = j

    while i > 0:
        while j <= m and pattern[i - 1] != pattern[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i
            j = border_pos[j]
        i -= 1
        j -= 1
        border_pos[i] = j

        print(f"pattern[{i}] = '{pattern[i] if i < len(pattern) else ''}', "
              f"border_pos[{i}] = {j}, shift = {shift}")

    print(f"\n[ Step 2: Finalize shift table from border positions ]")
    print(f"{'-'*50}")
    
    # Step 2: Fill in remaining shifts
    j = border_pos[0]
    for i in range(m + 1):
        if shift[i] == 0:
            shift[i] = j
        if i < m:
            print(f"shift[{i}] = {shift[i]} (good suffix: '{pattern[i:]}')")
    
    print(f"\n[ Final Good Suffix Table ]")
    print(f"{'-'*50}")
    print(f"{'Index':<6} {'Good Suffix':<20} {'Shift':<5}")
    print(f"{'-'*50}")
    for i in range(m):
        good_suffix = pattern[i:]
        print(f"{i:<6} {good_suffix:<20} {shift[i]}")
    
    return shift


# ▶️ Run the test
pattern = "ABCDABD"
print(f"Pattern: {pattern}")
good_suffix_shift = build_good_suffix_table(pattern)
