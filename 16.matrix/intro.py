"""
Matrix
"""

A = [
    [1, 2, 3],
    [4, 5, 6],
    [8, 9, 10]
]


row = 1

n = len(A) # no of rows

m = len(A[0]) # no of cols


# for i in range(m):
#     print(A[row-1][i])


# col = 3
# for i in range(n):
#     print(A[i][col-1])


# for i in range(n):
#     for j in range(m):
#         print(A[i][j], end=" ")
#     print()


# print the diagnol of a matrix

# r = 0
# c = 0

# while r < n and c < m:
#     print(A[r][c])
#     r+=1
#     c+=1
    

for i in range(min(m, n)):
    print(A[i][i])