def do_precomputation(A):
    running_sum = list()
    running_sum.append(A[0])
    for i in range(1, len(A)):
        running_sum.append(running_sum[i-1] + A[i])
    return running_sum

def solve(running_sum, i, j):
    if i == 0:
        return running_sum[j]
    return running_sum[j] - running_sum[i - 1]

if __name__ == '__main__':
    A = [1, 5, -1, 0, 4, 8, 4]
    print("Our Array is ", A)
    running_sum = do_precomputation(A)

    k = int(input())
    while k > 0:
        i, j = map(int, input().split())
        if i >= len(A) or j >= len(A):
            print(-1)
        print(solve(running_sum, i, j))
        k -= 1
