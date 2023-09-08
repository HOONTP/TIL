import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))
result = [1]*N
re_lst = [[lst[_]] for _ in range(N)]

for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            if result[i] < result[j]+1:
                result[i] = result[j]+1
                re_lst[i] = re_lst[j][:]
                re_lst[i].append(lst[i])

ind = result.index(max(result))
print(result[ind])
print(*re_lst[ind])