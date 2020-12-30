def solve(A):
    n = len(A)
    stack = list()
    
    next_greater_element = [0] * len(A)

    for idx, val in enumerate(A):
        if len(stack) == 0:
            stack.append(idx)
        else:
            cur = val
            
            while len(stack) != 0 and A[stack[-1]] < cur:
                x = stack[-1]
                stack.pop()
                next_greater_element[x] = cur
            stack.append(idx)
    
    while len(stack) != 0:
        x = stack[-1]
        stack.pop()
        next_greater_element[x] = None
        
    return next_greater_element



if __name__ == "__main__":
    A = [2, 1, 7, 4, 6, 8, 1, 9]
    
    ans = solve(A)
    print(ans)
    # next_greater_element_array = solve(A)
    # print(next_greater_element_array)
