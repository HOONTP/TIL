import sys
input = sys.stdin.readline

dij = [(1,0), (0,1), (-1,0), (0,-1)]
def deeping(n, sums, visted, cnt):
    global  mx_val
    if cnt == 4:
        if sums > mx_val:
            mx_val = sums
        return
    if mx*(4-cnt) + sums < mx_val:
        return
    for di, dj in dij:
        ni = n[0] + di
        nj = n[1] + dj
        if 0<= ni < N and 0<= nj < M and (ni, nj) not in visted:
            visted.append((ni, nj))
            sums += arr[ni][nj]
            deeping((ni,nj), sums, visted, cnt+1)
            visted.pop()
            sums -= arr[ni][nj]
    pass
def midline(n, sums):
    global mx_val
    mn = 999999999
    count = 1
    for di, dj in dij:
        ni = n[0] + di
        nj = n[1] + dj
        if 0<= ni < N and 0<= nj < M:
            sums += arr[ni][nj]
            count += 1
            if arr[ni][nj] < mn:
                mn = arr[ni][nj]
    if count == 5: #이게 개오바넹
        sums -= mn
    if sums > mx_val:
        mx_val = sums
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
mx = 0
for m in arr:
    mximum = max(m)
    if mx < mximum:
        mx = mximum
mx_val = 0
for i in range(N):
    for j in range(M):
        deeping((i,j), arr[i][j], [(i,j)], 1)
        midline((i,j), arr[i][j])
print(mx_val)