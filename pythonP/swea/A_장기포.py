T = int(input())
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
'''
하나를 건넜을 때 포를 잡을 수 있다면 잡아라. 잡았을 때 얘를 더 이상 체크하지 않는 방법은 외부의 배열을 끌어와서 변경해버리면 되나?
'''
def backT(S, n): # n은 3이면 그만 그만 ? 3번째 시행 후 그만
    global cnt
    if n == 3:
        return

    for k in range(4):
        for p in range(1, N):
            ni = S[0] + di[k] * p
            nj = S[1] + dj[k] * p
            if 0<= ni <N and 0<= nj <N:
                if arr[ni][nj] == 1:
                    for w in range(1, N):
                        i = ni + di[k] * w
                        j = nj + dj[k] * w
                        if 0<= i <N and 0<= j <N:
                            if arr[i][j] == 0 or arr[i][j] == 2:
                                backT((i, j), n+1)
                            elif arr[i][j] == 1 and (i, j) not in result:
                                cnt += 1
                                result.append((i, j))
                                backT((i, j), n+1)
                                break
                            else:
                                break
                        else:
                            break
                    else:
                        break
            else:#범위 오버시
                break

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                S = (i, j)
    cnt = 0
    result = []
    backT(S, 0)
    print(f'#{tc}', cnt)
