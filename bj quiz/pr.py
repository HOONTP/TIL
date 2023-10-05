import sys
input = sys.stdin.readline

def floyd(dist):
    # 모든 정점에 대한 최단 경로 갱신
    for k in range(1, V+1):
        for i in range(1, V+1):
            for j in range(1, V+1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

V, E = map(int, input().split())

arr = [[float('inf')]*(V+1) for _ in range(V+1)]

for __ in range(E):
    a, b, v = map(int, input().split())
    arr[a][b] = v

result = floyd(arr)
answer = float('inf')
for i in range(1, V+1):
    if result[i][i] < answer:
        answer = result[i][i]

if answer == float('inf'):
    print(-1)
else:
    print(answer)
