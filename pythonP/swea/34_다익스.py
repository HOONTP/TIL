import heapq

def dik(node):
    q = []
    heapq.heappush(q, (0, node))
    lst[node] = 0
    while q:
        w, n = heapq.heappop(q)
        if n == V:
            return
        for i in range(V+1):
            if arr[n][i] != 0 and lst[n] + arr[n][i] < lst[i]:
                lst[i] = lst[n] + arr[n][i]
                heapq.heappush(q, (lst[i], i))

for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        e, s, w = map(int, input().split())
        arr[e][s] = w

    lst = [float('inf')]*(V+1)
    # visted =[0]*(V+1)
    dik(0)
    print(f'#{t}', lst[V])
#
# import heapq
#
# def dik(node):
#     q = []
#     heapq.heappush(q, (0, node))
#     lst[node] = 0
#     while q:
#         w, n = heapq.heappop(q)
#         if n == V:
#             return
#         for i, weight in arr[n]:
#             if lst[n] + weight < lst[i]:
#                 lst[i] = lst[n] + weight
#                 heapq.heappush(q, (lst[i], i))
#
# for t in range(1, int(input())+1):
#     V, E = map(int, input().split())
#     # arr = [[0]*(V+1) for _ in range(V+1)]
#     # for _ in range(E):
#     #     e, s, w = map(int, input().split())
#     #     arr[e][s] = w
#     arr = [[] for _ in range(V+1)]
#     for _ in range(E):
#         e, s, w = map(int, input().split())
#         arr[e].append((s, w))
#
#     lst = [float('inf')]*(V+1)
#     # visted =[0]*(V+1)
#     dik(0)
#     print(f'#{t}', lst[V])