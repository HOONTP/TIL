T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a, b, c, d = map(int, input().split())# (a,b) -> (c,d) 진행 범위
    lst_mp = [list(map(int, input().split())) for _ in range(N)]

    sum = 0
    num = 0
    for i in range(a, c+1):#범위 합
        for j in range(b, d+1):
            sum += lst_mp[i][j]
            num += 1
    aver = sum // num

    result = 0
    for k in range(a, c+1):
        for l in range(b, d+1):
            if lst_mp[k][l] > aver:
                result += lst_mp[k][l] - aver#평균보다 클 경우
            else:
                result += aver - lst_mp[k][l]#평균보다 작을 경우

    print(f'#{tc}', result)