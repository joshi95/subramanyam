def solve(s):
    character_map = dict()
    n = len(s)

    max_length = 0

    start = 0
    end = 0

    while end < n:
        if s[end] not in character_map:
            character_map[s[end]] = end
            length = end - start + 1
            max_length = max(max_length, length)
            end += 1
        else:
            while s[end] in character_map:
                character_map.pop(s[start])
                start += 1
            character_map[s[end]] = end
            end += 1
    return max_length

if __name__ == '__main__':
    s = "ABCDEFGHRHYTHM"
    print(solve(s))
