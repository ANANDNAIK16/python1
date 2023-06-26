class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isSymmetric(root):
    if root is None:
        return None
    
    return isMirrror(root.left,root.right)

def isMirrror(l,r):
    if l is None and r is None:
        return True
    if l is None or r is None:
        return False
    
    return(l.val == r.val  and isMirrror(l.left, r.right) and isMirrror(l.right, r.left))


root = Node(4)
root.left = Node(5)
root.right = Node(5)
root.left.right = Node(6)
root.right.left = Node(6)

callingIsSymmentric = isSymmetric(root)

if callingIsSymmentric:
    print("Yes it is mirror")
else:
    print("not a mirror image")