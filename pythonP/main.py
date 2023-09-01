from collections import deque

T = int(input())
dij = [(-1,0), (0,1), (1,0), (0,-1)]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    q = deque()
    for i in range(N):
        arr.append(input())
        for j in range(M):
            if arr[i][j] == 'W':
                q.append(((i, j), 0))

    sums = 0
    visted = set()
    while q:
        n, cnt = q.popleft()
        for k in dij:
            if 0<= n[0] + k[0] < N and 0 <= n[1] + k[1] < M and arr[n[0] + k[0]][n[1] + k[1]] == 'L' and (n[0] + k[0], n[1] + k[1]) not in visted:
                sums += cnt + 1
                q.append(((n[0] + k[0], n[1] + k[1]), cnt + 1))
                visted.add((n[0] + k[0], n[1] + k[1]))

    print(f'#{tc}', sums)

    # ni = n[0] + k[0]
    # nj = n[1] + k[1]
    # if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 'L':
    #     arr[ni][nj] = 1
    #     sums += n[2] + 1
    #     q.append((ni, nj, n[2] + 1))



# T = int(input())

# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#
#     arr = [list(input()) for _ in range(N)]
#     # count_lst = [[-1]*M for _ in range(N)]
#     W_lst = []
#     L_lst = []
#
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 'W':
#                 W_lst.append((i, j))
#             else:
#                 L_lst.append((i, j))
#     # W_lst.sort(lambda x:x[0]+x[1])
#     # L_lst.sort(lambda x:x[0]+x[1])
#     # print(W_lst)
#     # print(L_lst)
#
#     sums = 0
#
#     for l in L_lst:
#         mid = 999999999
#         for k in W_lst:
#             di = k[0]-l[0]
#             dj = k[1]-l[1]
#             if abs(di)+abs(dj) < mid: #mid
#                 mid = abs(di)+abs(dj)
#             if mid == 1:
#                 break
#
#             # if count_lst[l[0]][l[1]] == 1:
#             #     break
#             # di = k[0]-l[0]
#             # dj = k[1]-l[1]
#             # if count_lst[l[0]][l[1]] == -1:
#             #     count_lst[l[0]][l[1]] = abs(di) + abs(dj)
#             #     continue
#             # if abs(di)+abs(dj) < count_lst[l[0]][l[1]]: #mid
#             #     # mid = abs(di)+abs(dj)
#             #     count_lst[l[0]][l[1]] = abs(di) + abs(dj)
#             # else:
#             #     break
#         sums += mid
#
#     # print(count_lst)
#     #
#     # for i in range(N):
#     #     for j in range(M):
#     #         if count_lst[i][j] != 999999999:
#     #             sums += count_lst[i][j]
#     print(f'#{tc}', sums)


# def bfs(q):
#     global sums