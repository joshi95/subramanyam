stack = list()

def push(x):
	global stack
	stack.append(x)
		
def pop():
	global stack
        if is_empty():
            return None
	stack.pop()

def peek():
	global stack
        if is_empty():
            return None
	return stack[len(stack) - 1]

def is_empty():
	global stack
	return len(stack) == 0

if __name__ == '__main__':
	push(10)
	push(5)
	push(77)
        
	print(peek())

	pop()
        print("Is stack empty ? ", is_empty())
	print(peek())


        pop()
        print("Is stack empty ? ", is_empty())
	print(peek())
        
        pop()
        print("Is stack empty ? ", is_empty())
	print(peek())

        print("Is stack empty ? ", is_empty())

	
