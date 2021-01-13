class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def solve(root, cur_level, max_level):
    if root is None:
        return

    if cur_level > max_level[0]:
        print(root.data)
        max_level[0] = cur_level

    solve(root.left, cur_level + 1, max_level)
    solve(root.right, cur_level + 1, max_level)


def checkIfValidBST(root):
    if root is None:
        return {
            "min_value": float("inf"),
            "max_value": float("-inf"),
            "isBST": True
        }

    if root.left is None and root.right is None:
        return {
            "min_value": root.data,
            "max_value": root.data,
            "isBST": True
        }

    left_ans = checkIfValidBST(root.left)
    right_ans = checkIfValidBST(root.right)

    if left_ans["isBST"] and right_ans["isBST"] and root.data > left_ans["max_value"] and root.data < right_ans["min_value"]:
        return {
            "min_value": min(root.data, left_ans["min_value"]),
            "max_value": max(root.data, right_ans["max_value"]),
            "isBST": True,
        }
    else:
        return {
            "min_value": min(root.data, left_ans["min_value"]),
            "max_value": max(root.data, right_ans["max_value"]),
            "isBST": False
        }


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(10)
    root.right = Node(15)

    root.left.right = Node(100)
    root.left.left = Node(50)
    max_level = [-1]
    ans = checkIfValidBST(root)
    print(ans["isBST"])
