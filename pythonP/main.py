import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

#프리 - 루좌우
#인오더 - 좌루우
#포스트 - 좌우루
def Pre_order(si, ei, so, eo):
    if si > ei:
        return
    root = Postorder[eo]
    mid = pos[root]
    # print(root, Inorder, Postorder, si, ei, so, eo)
    diff = ei - mid

    print(root, end=' ') # 5 - 1 - 1
    Pre_order(si, mid - 1, so, eo - diff - 1)
    Pre_order(mid + 1, ei , eo - diff , eo - 1)



N = int(input())
Inorder = list(map(int, input().split()))
Postorder = list(map(int, input().split()))
pos=[0]*(N+1)

#리스트의 인덱스를 미리 저장해두는 / 해당 값의 인덱스 위치에 그 리스트의 인덱스를 저장
for i in range(N):
    pos[Inorder[i]]=i

Pre_order(0, N-1, 0, N-1)
# print(*result)