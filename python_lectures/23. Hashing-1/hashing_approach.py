def solve(A, target):
    no_map = dict()
    for x in A:
        if target - x in no_map:
            return True
        no_map[x] = True
    return False

if __name__ == '__main__':
    A = [2, 3, 1, 4, 6]
    print(solve(A, 2))

