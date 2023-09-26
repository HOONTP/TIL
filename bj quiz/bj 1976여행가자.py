import sys
input = sys.stdin.readline

def find(x):
    if x == dic_[x]:
        return x
    dic_[x] = find(dic_[x])
    return dic_[x]

def uniset(a, b):
    A = find(a)
    B = find(b)

    if A != B:
        dic_[A] = B

N = int(input())
M = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
lst = list(map(int, input().split()))
dic_ = list(range(N))

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            uniset(i, j)

result = True
for i in range(M-1):
    if find(lst[i]-1) == find(lst[i+1]-1):
        pass
    else:
        result = False
        print('NO')
        break
if result:
    print('YES')