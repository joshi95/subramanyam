class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findHeight(root):
    if root is None:
        return 0
    
    if root.left == None and root.right == None:
        return 1
    
    lh = findHeight(root.left)
    rh = findHeight(root.right)
    return max(lh, rh) + 1

def printNodesAtHeight(root, ht):
    if root is None:
        return
    
    if ht == 1:
        print(root.data, end=" ")
        return
    
    printNodesAtHeight(root.left, ht - 1)
    printNodesAtHeight(root.right, ht - 1)

def printLevelWise(root):
    if root is None:
        return

    ht = findHeight(root)

    for h in range(1, ht+1):
        print("level", h)
        printNodesAtHeight(root, h)
        print()


def PrintLevelOrderQueue(root):
    if root is None:
        return
    
    queue = list()
    queue.append(root)

    while len(queue) > 0:
        x = queue.pop(0)
        print(x.data, end=" ")

        if x.left is not None:
            queue.append(x.left)
        
        if x.right is not None:
            queue.append(x.right)
    
    

if __name__ == "__main__":
    root = Node(5)
    root.left = Node(10)
    root.right = Node(15)

    root.left.right = Node(100)
    root.left.left = Node(50)

    PrintLevelOrderQueue(root)
    