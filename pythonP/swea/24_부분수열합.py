def binary():
    global cnt
    for i in range(1 << N):
        case = []
        for j in range(N):
            if i & (1 << j):
                case.append(lst[j])
        if sum(case) == M:
            cnt += 1


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    for i in lst: # 이 로직 쓰려다가 index에러 계속 남
        if i > M:
            j = lst.index(i)
            lst.pop(j)
    N = len(lst)

    cnt = 0
    binary()
    print(f'#{tc}', cnt)