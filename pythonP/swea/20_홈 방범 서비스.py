# '''
# K * K + (K - 1)*(K - 1)
# P의 크기마다 세로열 P 가로열 P 크기를 인덱스로 조정해서 체크 할 수 있음
# for i in range(-P+1, P):
#     for j in range(-P+1-i, P-i):
#         if arr[i][j] == 1:
#             sums += M
# bfs 불가! 외각 어쩔거
# '''
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    mn = 0
    for i in range(N):
        for j in range(N):
            for P in range(N+1, 0, -1):
                sums = 0
                cost = P * P + (P - 1) * (P - 1)
                if cost > mn:
                    for k in range(-P + 1, P):
                        for l in range(-P + 1 + abs(k), P - abs(k)):
                            ni = i + k
                            nj = j + l
                            if 0<= ni <N and 0<= nj <N and arr[ni][nj] == 1:
                                sums += M
                    if sums >= cost:
                        home = sums // M
                        if mn < home:
                            mn = home
                            break
    print(f'#{tc}', mn)
