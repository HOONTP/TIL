dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
R, C, K = map(int, input().split())

MAPS = list(input() for _ in range(R))
def backT(x, y, visited, cnt):
    global result

    if x == 0 and y == C-1 and cnt == K:
        result += 1
        return
    if cnt >= K:
        return

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and MAPS[nx][ny] != 'T' and not visited[nx][ny]:
            visited[nx][ny] = True
            backT(nx, ny, visited, cnt + 1)
            visited[nx][ny] = False


    return

visited = list([0]*C for _ in range(R))

visited[R-1][0] = 1
result = 0
backT(R-1, 0, visited, 1) # 시작점이 1인게 맘에 들지 않음.. ㅠ
print(result)