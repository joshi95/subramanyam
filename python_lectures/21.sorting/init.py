

def selection_sort(A):
    # [1, 8, 4, 2, 3, 8]

    n = len(A)
    for i in range(n):
        min_ele = A[i]
        min_ele_idx = i
        for idx in range(i, len(A)):
            if A[idx] < min_ele:
                min_ele = A[idx]
                min_ele_idx = idx
        A[i], A[min_ele_idx] = A[min_ele_idx], A[i]
    return A


def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A


if __name__ == "__main__":
    A = [6, 7, 1, 2, 4, 5, 6]
    print(bubble_sort(A))
