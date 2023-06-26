class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1

def checkBalacedOrNot(root):
    if root is None:
        return True
    
    leftHeight = height(root.left)
    rightHeight = height(root.right)

    if abs(leftHeight-rightHeight) <=1 and checkBalacedOrNot(root.left) and checkBalacedOrNot(root.right):
        return True
    else:
        return False


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)

a = checkBalacedOrNot(root)

if a:
    print("tree is balanced")
else:
    print("tree ain't balanced")