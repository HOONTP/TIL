T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tre = [0]*(N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        tre[a] = b
    for i in range(N-M, 0, -1):
        if i*2+1 <= N:
            tre[i] = tre[i*2] + tre[i*2+1]
        else:
            tre[i] = tre[i*2]
    print(f'#{tc}', tre[L])