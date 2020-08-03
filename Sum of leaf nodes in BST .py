s=0
def sumOfLeafNodes(root):
    s=0
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data
    #print(s,end=" ")
    return  sumOfLeafNodes(root.left)+sumOfLeafNodes(root.right)
