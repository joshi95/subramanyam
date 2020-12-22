"""
Given 2 arrays sorted arrays A and B. 
We need to merge them and get sorted Array C.
A = [1, 4, 6, 7, 8, 9]
B = [3, 5, 14, 18]
C = [1, 3, 4, 5, 6, 7, 8, 9, 14, 18]
"""


def Merge2SortedArray(A, B): C = list()
    for x in A:
        C.append(x)

    for x in B:
        C.append(x)

    C.sort() # O(Nlogn)
    return C

"""
O(n) time complexity
"""

def Merge2SortedArray2(A, B):
    n = len(A)
    m = len(B)

    p1 = 0
    p2 = 0

    C = list()

    while p1 < n and p2 < m:
        if A[p1] < B[p2]:
            C.append(A[p1])
            p1 += 1
        else:
            C.append(B[p2])
            p2 += 1

    while p1 < n:
        C.append(A[p1])
        p1 += 1

    while p2 < m:
        C.append(B[p2])
        p2 += 1

    return C





