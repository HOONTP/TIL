import sys
input = sys.stdin.readline

dij = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def backT(n, visted, cnt):
    global max
    if cnt == 26:
        print(cnt)
        exit()

    if visted in max_lst[n[0]][n[1]]:
        # print(visted)
        # print(max_lst)
        return
    else:
        max_lst[n[0]][n[1]].append(visted)

    for k in dij:
        ni = n[0] + k[0]
        nj = n[1] + k[1]
        if 0<= ni <R and 0<= nj <C and arr[ni][nj] not in visted: # and max_lst[ni][nj] < cnt+1
            # print(visted)
            visted.append(arr[ni][nj])
            A = visted[:]
            backT((ni,nj), A, cnt + 1)
            visted.pop()
        else:
            if max < cnt:
                max = cnt

R, C = map(int, input().split())

arr = [input().strip() for _ in range(R)]

max_lst = [[[] for _ in range(C)] for _ in range(R)]
max = 0

backT((0,0), [arr[0][0]], 1)
print(max)
print(max_lst)
