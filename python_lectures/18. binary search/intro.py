"""
1. Linear Search
2. Binary Search - Binary search works only for sorted solution space / list.
"""


# def binarySearch(A, target):
#     """
#     binarySearch
#     Args:
#     A: List of integer
#     target: integer i want to search
#     """
#     left = 0
#     right = len(A) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if A[mid] == target:
#             return mid
#         elif A[mid] > target:
#             right = mid - 1
#         else:
#             left = mid + 1

#     return None


# if __name__ == "__main__":
#     A = [1, 22, 44, 55, 66, 77, 88, 120, 135, 151]
#     target = 15108

#     print(binarySearch(A, target))


# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         count = 0
#         bit = 1
#         for i in range(32):
#             if n & bit != 0:
#                 count+=1
#             bit = bit << 1
#         return count


# if __name__ == "__main__":
#     s = Solution()
#     print(s.plusOne([0,0,0]))


# upper and lower bound





def lowerbound(A, target) -> int:
    n = len(A)

    left = 0
    right = n - 1
    
    ans = -1

    while left <= right:
        mid = (left + right) >> 1 # or (left + right) // 2
        if A[mid] == target:
            ans = mid
            right = mid - 1
        elif A[mid] > target:
            right = mid - 1
        elif A[mid] < target:
            left = mid + 1
    
    return ans

def upperbound(A, target) -> int:
    n = len(A)

    left = 0
    right = n - 1
    
    ans = -1

    while left <= right:
        mid = (left + right) >> 1 # or (left + right) // 2
        if A[mid] == target:
            ans = mid
            left = mid + 1
        elif A[mid] > target:
            right = mid - 1
        elif A[mid] < target:
            left = mid + 1
    
    return ans


if __name__ == "__main__":
    A = [1, 1, 1, 1, 2,2,2,2,2,2, 3, 3, 4, 5, 5]
    x = 2
    print(upperbound(A, x) - lowerbound(A, x) + 1)
    #2*log(n) = log(n)