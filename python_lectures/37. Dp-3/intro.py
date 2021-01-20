def generateSubsequence(arr, idx, current_subsequence):
    
    if idx == len(arr):
        print(current_subsequence)
        return

    # i am taking element at idx position
    current_subsequence.append(arr[idx])
    generateSubsequence(arr, idx + 1, current_subsequence)

    # if i don't take element at idx position
    current_subsequence.pop()
    generateSubsequence(arr, idx + 1, current_subsequence)



def maxLengthSubsequence(arr):
    n = len(arr)
    dp = [1] * n

    for j in range(1, n):
        for i in range(0, j):
            if arr[i] < arr[j]:
                dp[j] = max(dp[j], dp[i] + 1)
    
    return max(dp)


def findMaxSumSubarray(arr):
    n = len(arr)
    max_sum = 0
    for i in range(0, n):
        for j in range(i, n):
            sum = presum[j] - presum[i-1]
            max_sum = max(max_sum, sum)
    return max_sum
        

def kadaneAlgo(arr):
    cur_sum = arr[0]
    max_sum = arr[0]
    for i in range(1, len(arr)):
        cur_sum = max(cur_sum + arr[i], arr[i])
        max_sum = max(cur_sum, max_sum)
    return max_sum




if __name__ == "__main__":
    a = [100, 2, 3,4, 5]
    print(maxLengthSubsequence(a))