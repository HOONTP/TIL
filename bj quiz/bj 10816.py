import sys
input = sys.stdin.readline

N = int(input())
lst_N = list(map(int, input().split()))
M = int(input())
lst_M = list(map(int, input().split()))

lst_N.sort()

dic_ = {}
i = 0

while i < N: # dict에 값, 갯수 저장
    cnt = 1
    try:
        while lst_N[i] == lst_N[i+1]:
            cnt += 1
            i += 1
    except IndexError:
        pass
    dic_[lst_N[i]] = cnt
    i += 1

for it in lst_M:
    if it in dic_:
        print(dic_[it], end=' ')
    else:
        print(0, end=' ')