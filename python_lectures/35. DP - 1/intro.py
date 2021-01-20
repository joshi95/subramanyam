


def Fib(no):
    if no == 0:
        return 0
    
    if no == 1:
        return 1

    return Fib(no - 1) + Fib(no - 2)

if __name__ == "__main__":
    print(Fib(135))


# Tabulation 
def FibBottomUp(n):
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i - 2]
    
    return dp[n]

# Memoization
def Fib(no, dp):
    if no == 0:
        return 0
    
    if no == 1:
        return 1

    if dp[no] is not None:
        return dp[no]
        

    ans = Fib(no - 1, dp) + Fib(no - 2, dp)
    dp[no] = ans
    return ans

if __name__ == "__main__":
    dp = [None] * 10005
    print(Fib(135, dp))