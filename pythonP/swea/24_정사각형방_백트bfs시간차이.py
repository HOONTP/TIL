dij = [(-1,0), (1, 0), (0, 1), (0, -1)]

T = int(input())

def dbdbfs(S):
    global mx
    global result

    q = []
    q.append(S)
    visted = []
    visted.append(S)
    cnt = 1

    while q:
        n = q.pop()

        for k in dij:
            ni = n[0] + k[0]
            nj = n[1] + k[1]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[n[0]][n[1]] + 1:
                q.append((ni, nj))
                visted.append((ni, nj))
                cnt += 1
    if mx < cnt:
        mx = cnt
        result = [arr[S[0]][S[1]], cnt]
    elif mx == cnt:
        if result[0] > arr[S[0]][S[1]]:
            result = [arr[S[0]][S[1]], cnt]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    mx = 0
    result = []

    for i in range(N):
        for j in range(N):
            for k in dij:
                ni = i + k[0]
                nj = j + k[1]
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] + 1 == arr[i][j]:
                    break
            else:
                dbdbfs((i,j))
    print(f'#{tc}', *result)

# 백트래킹으로 순회하면 N이 커졌을 때 매우 느림. 재귀라서 그런듯?
# dij = [(-1,0), (1, 0), (0, 1), (0, -1)]
#
# T = int(input())
#
# def backT(start, S, cnt):
#     global mx
#     global result
#
#     for k in dij:
#         ni = S[0] + k[0]
#         nj = S[1] + k[1]
#         if 0<= ni <N and 0<= nj <N and (ni, nj) not in visted and arr[ni][nj] == arr[S[0]][S[1]] + 1:
#             visted.append((ni, nj))
#             backT(start, (ni, nj), cnt+1)
#             return
#     else:
#         if mx < cnt:
#             mx = cnt
#             result = [arr[start[0]][start[1]], mx]
#         elif mx == cnt:
#             if result[0] > arr[start[0]][start[1]]:
#                 result = [arr[start[0]][start[1]], mx]
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     mx = 0
#     result = []
#     visted = []
#     for i in range(N):
#         for j in range(N):
#             for k in dij:
#                 ni = i + k[0]
#                 nj = j + k[1]
#                 if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] + 1 == arr[i][j]:
#                     break
#             else:
#
#                 if (i, j) not in visted:
#                     visted.append((i,j))
#                     backT((i,j), (i,j), 1)
#     print(f'#{tc}', *result)