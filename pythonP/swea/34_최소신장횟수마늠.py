import heapq
for t in range(1, int(input())+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    E = float(input())

    # N개의 좌표가 있고

    for i in range(N):
        for j in range(N):
            value = ((X[i]-X[j])**2 + (Y[i]-Y[j])**2)
            arr[i][j] = value
            arr[j][i] = value
    q = []
    sums = 0
    visited = [0]*N

    heapq.heappush(q, (0, 0))
    while q:
        w, n = heapq.heappop(q)
        if visited[n]:
            continue
        visited[n] = 1
        sums += w
        for i in range(N):
            if n == i or visited[i]:
                continue
            heapq.heappush(q, (arr[n][i], i))
    print(f'#{t}', round(sums*E))