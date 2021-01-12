def find(root, target):
    if root is None:
        return False

    if root.val == target:
        return True

    if root.val < target:
        return find(root.right, target)
    else:
        return find(root.left, target)


counter = 0


def findKthSmallestValue(root, k):
    global counter
    if root is None:
        return None

    if counter == k:
        return root.val

    findKthSmallestValue(root.left, k)

    # logic
    counter += 1

    findKthSmallestValue(root.right, k)
