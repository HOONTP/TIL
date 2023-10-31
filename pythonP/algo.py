import sys
input = sys.stdin.readline

def floyd(dist):
    # 모든 정점에 대한 최단 경로 갱신
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != 0 and dist[k][j] != 0:
                    if i != j:
                        if dist[i][j] == 0:
                            dist[i][j] = dist[i][k] + dist[k][j]
                            lst[i][j] = lst[i][k] + lst[k][j]
                        elif dist[i][k] + dist[k][j] < dist[i][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]
                            lst[i][j] = lst[i][k] + lst[k][j]
    return dist

V = int(input())
E = int(input())

arr = [[0]*(V) for _ in range(V)]
lst = [[[k+1] for k in range(V)] for _ in range(V)]
for __ in range(E):
    a, b, v = map(int, input().split())
    if arr[a-1][b-1] == 0 or v < arr[a-1][b-1]:
        arr[a-1][b-1] = v
result = floyd(arr)
print(lst)
for re in result:
    print(*re)
for i in range(V):
    for j in range(V):
        if result[i][j] == 0:
            print(0)
        else:
            print(len(lst[i][j])+1, i+1 ,*lst[i][j])