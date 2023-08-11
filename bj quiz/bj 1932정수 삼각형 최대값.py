import sys
input = sys.stdin.readline

def mx_sums(n):
    dic_[0, 0] = arr[0][0]

    for i in range(1, n):
        dic_[i, 0] = dic_[i-1, 0] + arr[i][0]
        dic_[i, i] = dic_[i-1, i-1] + arr[i][i]
        for j in range(1, i):
            dic_[i, j] = max(dic_[i-1, j-1] + arr[i][j], dic_[i-1, j] + arr[i][j])

    return

N = int(input())
arr = [[0]*N for _ in range(N)]
dic_ = {} #좌표를 알고 싶다면 리스트가 편할까?

for _ in range(N):
    lst = list(map(int, input().split()))
    for i in range(len(lst)):
        arr[_][i] = lst[i]

mx_sums(N)
mx_val = 0
for j in range(N):
    if mx_val < dic_[N-1, j]:
        mx_val = dic_[N-1, j]

print(mx_val)