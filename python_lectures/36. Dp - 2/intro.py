
# def solve(starting_position, n, dp):
#     if starting_position == n:
#         return 1
#     if starting_position > n:
#         return 0
    
#     if dp[starting_position] != None:
#         return dp[starting_position]

#     left = solve(starting_position + 1, n, dp)
#     right = solve(starting_position + 2, n, dp)

#     dp[starting_position] = left + right
#     return dp[starting_position]


def solve(str1, str2, idx1, idx2, dp):

    if idx1 == len(str1) or idx2 == len(str2):
        return 0

    if dp[idx1][idx2] is not None:
        return dp[idx1][idx2]

    ans = 0
    if str1[idx1] == str2[idx2]:
        ans = 1 + solve(str1, str2, idx1 + 1, idx2 + 1, dp)
    else:
        ans = max(solve(str1, str2, idx1 + 1, idx2, dp), solve(str1, str2, idx1, idx2 + 1, dp))
    dp[idx1][idx2] = ans
    return dp[idx1][idx2]

if __name__ == "__main__":
    n = 4
    dp = [[None for _ in range(1000)] for _ in range(1000)]
    print(solve("ABCED", "XEDCBEADDECED", 0, 0, dp))

