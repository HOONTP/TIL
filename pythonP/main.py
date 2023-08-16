T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    visited = [0] * 400
    for i in range(N):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s
        for j in range(s - 1, e):
            visited[j] += 1

    print(f'#{tc} {max(visited)}')
