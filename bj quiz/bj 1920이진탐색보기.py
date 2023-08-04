import sys
input = sys.stdin.readline

N = int(input())
N_lst = list(map(int, input().split()))
N_lst.sort()

M = int(input())
M_lst = list(map(int, input().split()))

for i in range(M):
    sp = 0
    ep = N - 1
    mid_p = int((ep + sp) / 2)
    while sp <= ep:
        if N_lst[mid_p] == M_lst[i]:
            print(1)
            break
        elif N_lst[mid_p] < M_lst[i]:
            sp = mid_p+1
        else:
            ep = mid_p-1
        mid_p = (ep + sp) // 2
    else:
        print(0)
