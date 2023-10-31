import sys
input = sys.stdin.readline
import heapq

def distance(A, B):
    sums = ((A[0]-B[0])**2 + (A[1]-B[1])**2)**(0.5)
    return sums

def dijk(n):
    q = []
    heapq.heappush(q, (0, n))

    while q:
        w, node = heapq.heappop(q)

        for i in range(N):
            if node != i and n != i:
                if w + lst[node][i] < result[n][i]:
                pass

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(float, input().split())))
print(arr)

lst = [[0]*N for _ in range(N)]
for i in range(N):
    min_value = float('inf')
    for j in range(N):
        if i != j:
            dist = distance(arr[i],arr[j])
            lst[i][j] = round(dist, 3)

result = [[0]*N for _ in range(N)]
print(lst)