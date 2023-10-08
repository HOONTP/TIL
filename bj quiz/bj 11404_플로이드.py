import sys
input = sys.stdin.readline

def floyd(dist):
    for k in range(V):
        for i in range(V):
            if k == i:
                continue
            for j in range(V):
                if i != j:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]


    return dist

V = int(input())
E = int(input())

arr = [[float('inf')]*V for _ in range(V)]

for __ in range(E):
    a, b, v = map(int, input().split())
    if arr[a-1][b-1] > v:
        arr[a-1][b-1] = v

result = floyd(arr)# arr을 넣어주고 위에서 dist로 사용하고 result에 부여했는데
for i in range(V): # 세 가지다 같은 리스트로 판단하는 듯?
    for j in range(V):
        if arr[i][j] == float('inf'):
            arr[i][j] = 0
for i in result:
    print(*i)