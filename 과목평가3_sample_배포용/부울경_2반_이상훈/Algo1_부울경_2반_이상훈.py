T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:#범위 이내에서만 조건문 시작
                    if arr[i][j] <= arr[ni][nj]:#주변이 더 클 경우 탈출
                        break
            else:#for문이 정상적으로 모두 순회할 경우 호출(모든 방향이 더 작을 경우만)
                cnt += 1
    print(f'#{tc}', cnt)