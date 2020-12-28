def solve(A):
    n = len(A)
    XX = sum(A) - n*(n+1)//2 # Y - X

    sum1 = 0 # Sum of square of n natural no
    for i in range(1, n + 1):
        sum1 += i * i

    sum2 = 0 # Sum of square of array element
    for i in A:
        sum2 += i * i

    YY = sum2 - sum1 # Y^2 - X^2

    ZZ = YY // XX # Y + X

    _Y = (ZZ + XX) // 2
    _X = ZZ - _Y

    return _X, _Y


if __name__ == '__main__':
    A = [1, 2, 3, 3, 4]
    print(solve(A))
    
