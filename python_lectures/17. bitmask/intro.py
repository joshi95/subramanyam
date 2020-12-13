"""
decimal to binary
"""


def ConvertDecimalToBinary(no):
    binary_string = ""
    while no > 0:
        rem = no % 2
        binary_string += str(rem)
        no //= 2
    
    return binary_string[::-1]


if __name__ == "__main__":
    print(ConvertDecimalToBinary(32))


def solve(A):
    ans = A[0]
    for i in range(1, len(A)):
        ans = ans ^ A[i]
    return ans