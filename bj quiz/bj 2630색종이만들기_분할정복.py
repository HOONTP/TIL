import sys
input = sys.stdin.readline

def isright(n, k): # n = 0 , 0 k = N-1, N-1
    global one_cnt
    global zero_cnt
    if binar0(n, k) == 1:
        zero_cnt += 1
        return
    elif binar1(n, k) == 1:
        one_cnt += 1
        return
    else:
        i_mid = (n[0]+k[0]) // 2
        j_mid = (n[1]+k[1]) // 2
        isright(n, (i_mid,j_mid))
        isright((n[0], j_mid), (i_mid, k[1]))
        isright((i_mid, n[1]), (k[0], j_mid))
        isright((i_mid,j_mid), k)

def binar0(n, k):
    for i in range(n[0], k[0]):
        for j in range(n[1], k[1]):
            if arr[i][j] != 0:
                return 0
    return 1

def binar1(n, k):
    for i in range(n[0], k[0]):
        for j in range(n[1], k[1]):
            if arr[i][j] != 1:
                return 0
    return 1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

zero_cnt = 0
one_cnt = 0
isright((0,0), (N ,N))

print(zero_cnt)
print(one_cnt)