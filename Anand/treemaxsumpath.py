class Head:
    max_sum = float('-inf')

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

    Head.max_sum = max(Head.max_sum, maxFromTop)

    return maxx

head = Head(10)

head.left = Head(-10)
head.left.left = Head(5)
head.left.right = Head(-1)
head.left.left.left = Head(15)
head.left.left.right = Head(8)

head.right = Head(25)
head.right.right = Head(-24)
head.right.left = Head(6)


treeMaxSumPath(head)

print(Head.max_sum)