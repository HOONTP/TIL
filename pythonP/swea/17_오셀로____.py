import pprint
T = int(input())
di = [-1,-1,0,1,1,1,0,-1]
dj = [0,1,1,1,0,-1,-1,-1]#위로 시작 시계방향
def bfs(A):
    if A[2] == 1:
        S = 'B'
        targ = 'W'
        arr[A[0]][A[1]] = S
    else:
        S = 'W'
        targ = 'B'
        arr[A[0]][A[1]] = S

    n = A
    for k in range(8):
        p = 1
        stack = []  # 변경할 좌표 임시 저장 / 이걸 왜 위에다가 지정해가지고 ㅡ ㅡ
        while True:
            ni = n[0] + di[k] * p # 각 방향으로 계속 진행 p를 증가시키며.
            nj = n[1] + dj[k] * p
            if 0< ni <=N and 0< nj <=N:
                if arr[ni][nj] == targ: # 타겟을 만나면 스택에 저장
                    stack.append((ni, nj))
                elif arr[ni][nj] == S:  # 시작점 문자를 만나면 스택을 비우면서 바꿈
                    # print(stack)
                    while stack:
                        x, y = stack.pop()
                        arr[x][y] = S
                    break     # 돌 사이에만 있으면 다 바뀌는 줄 알고 이거 안 넣어서 개고생했네 ㅡ
                else:
                    break
            else: # 범위가 끝에 닿으면 탈출
                break
            p += 1
    # print(arr)

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    # 중간 시작 값 지정
    arr[N // 2][N // 2] = 'W'
    arr[N // 2 + 1][N // 2 + 1] = 'W'
    arr[N // 2 + 1][N // 2] = 'B'
    arr[N // 2][N // 2 + 1] = 'B'
    # pprint.pprint(arr)

    for _ in range(M):
        lst = list(map(int, input().split()))
        bfs(lst)
    W_sum = 0
    B_sum = 0
    # pprint.pprint(arr)
    for i in arr:
        W_sum += i.count('W')
        B_sum += i.count('B')
    print(f'#{tc}', B_sum, W_sum)