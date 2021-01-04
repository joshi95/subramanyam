queue = list()

def enqueu(x):
    global queue
    queue.append(x)

def dequeu():
    global queue
    if is_empty():
        return
    x = queue[0]
    queue.pop(0)
    return x

def is_empty():
    global queue
    return len(queue) == 0

if __name__ == "__main__":
    enqueu(6)
    enqueu(99)
    print(dequeu())
    print(dequeu())
    print(queue)