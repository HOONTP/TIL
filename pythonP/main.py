import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

#프리 - 루좌우
#인오더 - 좌루우
#포스트 - 좌우루
def Pre_order(inorder, s, e):
    if not inorder:
        return []
    # print(inorder, Postorder, s, e)
    root = Postorder[e]
    mid = inorder.index(root)

    left_in = inorder[:mid]
    right_in = inorder[mid+1:]

    left_ = Pre_order(left_in, s, s+mid-1)
    right_ = Pre_order(right_in, s+mid, e-1)

    return [root] + left_ + right_


N = int(input())
Inorder = list(map(int, input().split()))
Postorder = list(map(int, input().split()))

result = Pre_order(Inorder, 0, N-1)
print(*result)