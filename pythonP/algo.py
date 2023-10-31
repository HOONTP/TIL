import sys
input = sys.stdin.read
sys.setrecursionlimit(10**9)

class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build(preorder):
    if not preorder:
        return None

    root_value = preorder[0]
    root = Tree(root_value)

    if len(preorder) > 1:
        index = 1
        while index < len(preorder) and preorder[index] <= root_value:
            index += 1

        root.left = build(preorder[1:index])
        root.right = build(preorder[index:])
    return root

def SearchTree(root):
    if root is None:
        return []
    SearchTree(root.left)
    SearchTree(root.right)
    print(root.value)


In = input().strip()
arr = list(map(int, In.split()))
# print(arr)
root = build(arr)
# print(root)
result = SearchTree(root)
# for i in result:
#     print(i)