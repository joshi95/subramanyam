def merge(A, start1, end1, start2, end2):
    p1 = start1
    p2 = start2

    temp = list()
    while p1 <= end1 and p2 <= end2:
        if A[p1] < A[p2]:
           temp.append(A[p1])
           p1 += 1
        else:
            temp.append(A[p2])
            p2 += 1

    while p1 <= end1:
        temp.append(A[p1])
        p1 += 1

    while p2 <= end2:
        temp.append(A[p2])
        p2 += 1

    idx = 0
    while idx < len(temp):
        A[start1 + idx] = temp[idx]
        idx += 1

def mergeSort(A, left, right):
    if left >= right:
        return

    mid = (left + right) >> 1
    mergeSort(A, left, mid)
    mergeSort(A, mid + 1, right)

    merge(A, left, mid, mid + 1, right)

if __name__ == '__main__':
    #yypA = [5, 6, 2, 3, 66, 7, 1, 2,2, 34, 5]
    A = [5,4,3,2,1]
    print("Unsorted Array is ", A)
    mergeSort(A, 0, len(A) - 1)
    print("Sorted Array is ", A)

