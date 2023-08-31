T = int(input())

for tc in range(1, T+1):
    N = int(input())
    time = []
    for _ in range(N):
        time.append(list(map(int, input().split())))

    time.sort()

    cnt = 1
    s = time[0][0]
    e = time[0][1]
    for i in range(1, N):
        if time[i][0] >= e:
            e = time[i][1]
            cnt += 1
        elif time[i][1] < e:
            e = time[i][1]
    print(f'#{tc}', cnt)