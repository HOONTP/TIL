T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = []
    for _ in range(N):
        A, M = input().split()
        m = int(M)
        for i in range(m):
            lst.append(A)

    cnt = 0

    print(f'#{tc}')
    for i in lst:
        print(i, end='')
        cnt += 1
        if cnt == 10:
            print()
            cnt = 0
    if cnt != 0: # 여기 걍 print() 써도 제출된다.
        print()