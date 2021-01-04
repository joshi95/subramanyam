# ===============================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ===============================

head = None

def addNodeAtEnd(x):
    """
    You have a head of a linked list and you want to add 
    a node with value x at the end of the linked list. 
    or
    Adding a node at the tail of the linked list.
    """

    global head

    if head is None:
        head = Node(x)
        return
    
    cur = head
    while cur.next != None:
        cur = cur.next
    
    cur.next = Node(x)

def printLinkedList():
    global head

    cur = head
    while cur != None:
        print(cur.data)
        cur = cur.next

def addNodeAtBegining(x):
    global head

    if head is None:
        head = Node(x)
        return
    
    node = Node(x)
    node.next = head
    head = node

def addNodeInMiddle(n, x):
    if n <= 0:
        return

    global head

    cnt = 1
    cur = head
    while cnt != n:
        cur = cur.next
        cnt += 1

    cur_neighbor = cur.next
    new_node = Node(x)

    cur.next = new_node
    new_node.next = cur_neighbor

    

def deleteTailNode():
    global head

    if head is None:
        return

    prev = None
    cur = head

    while cur.next != None:
        prev = cur
        cur = cur.next

    prev.next = None


def deleteAtHead():
    global head
    if head is None:
        return

    head = head.next



if __name__ == "__main__":
    addNodeAtBegining(5)
    addNodeAtBegining(25)
    
    addNodeAtEnd(10)
    addNodeAtEnd(100)
    addNodeAtEnd(200)
    addNodeAtEnd(500)
    
    printLinkedList()
    print("before deletion")
    

    # deleteTailNode()
    # deleteTailNode()
    # deleteTailNode()   
    deleteAtHead()
    printLinkedList()
    print("after deletion")
    