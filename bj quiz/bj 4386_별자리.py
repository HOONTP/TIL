import sys
input = sys.stdin.readline
import heapq

def distance(A, B):
    sums = ((A[0]-B[0])**2 + (A[1]-B[1])**2)**(0.5)
    return sums

def dijk():
    sums = 0
    count = 0
    while q:
        way, a, b = heapq.heappop(q)
        # print(way, a, b)
        if uni_set(a, b):
            sums += round(way, 3)
            count += 1
        if count == N-1:
            return round(sums, 2)

    return round(sums, 2)

def uni_find(x):
    if dict_[x] == x:
        return x
    dict_[x] = uni_find(dict_[x])
    return dict_[x]

def uni_set(a, b):
    A = uni_find(a)
    B = uni_find(b)

    if A == B:
        return False
    else:
        dict_[B] = A
        dict_[b] = A
        return True

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(float, input().split())))

dict_ = list(range(N))
q = []
for i in range(N):
    min_value = float('inf')
    for j in range(N):
        if i != j:
            dist = distance(arr[i], arr[j])
            heapq.heappush(q, (dist, i, j))

result = dijk()
print(result)