import sys
input = sys.stdin.readline

def floyd(dist):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if i != j:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                else:
                    dist[i][j] = 0

    return dist

V = int(input())
E = int(input())

arr = [[float('inf')]*V for _ in range(V)]

for __ in range(E):
    a, b, v = map(int, input().split())
    if arr[a-1][b-1] != 0:
        if arr[a-1][b-1] > v:
            arr[a-1][b-1] = v
    else:
        arr[a - 1][b - 1] = v
print(arr)
result = floyd(arr)
print(result)
for i in result:
    print(*i)