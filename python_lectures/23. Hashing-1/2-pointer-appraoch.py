def solve(A):
    A.sort()
    left = 0
    right = len(A) - 1

    target = 5
    while left < right:
        _sum = A[left] + A[right]
        if _sum > target:
            right -= 1
        elif _sum < target:
            left += 1
        elif _sum == target:
            return True
    return False

if __name__ == '__main__':
    A = [2, 3, 4, 1, 6]
    print(solve(A))
