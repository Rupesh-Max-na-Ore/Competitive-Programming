def generate_permutations(freq_map, path, length, result):
    if len(path) == length:
        result.append("".join(path))
        return
    for ch in sorted(freq_map.keys()):  # Sorted to ensure lexicographic order
        if freq_map[ch] > 0:
            freq_map[ch] -= 1
            path.append(ch)

            generate_permutations(freq_map, path, length, result)

            path.pop()  # Backtrack
            freq_map[ch] += 1


def solve(s):
    freq_map = {}
    for ch in s:
        freq_map[ch] = freq_map.get(ch, 0) + 1

    result = []
    generate_permutations(freq_map, [], len(s), result)

    print(len(result))
    for word in result:
        print(word)


# Input
s = input()
solve(s)
