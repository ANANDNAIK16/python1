class Head:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def treeMaxSumPath(rootNode):
    if rootNode is None:
        return 0

    leftSum = treeMaxSumPath(rootNode.left)
    rightSum = treeMaxSumPath(rootNode.right)

    maxx = max(max(leftSum, rightSum) + rootNode.value, rootNode.value)
    maxFromTop = max(maxx, leftSum + rightSum + rootNode.value)

    treeMaxSumPath.max_sum = max(treeMaxSumPath.max_sum, maxFromTop)

    return maxx

head = Head(1)
head.left = Head(2)
head.left.left = Head(4)
head.right = Head(3)
head.right.left = Head(5)
head.right.right = Head(6)
head.right.left.left = Head(7)

treeMaxSumPath.max_sum = float('-inf')
treeMaxSumPath(head)

print(treeMaxSumPath.max_sum)

