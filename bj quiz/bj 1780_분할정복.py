import sys
input = sys.stdin.readline

def sepa(x, y, n):
    before = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if before != arr[i][j]:
                dl = n // 3
                for k in range(3):
                    for l in range(3):
                        sepa(x + dl * k, y + dl * l, dl)
                return
    if before == -1:
        counting[0] += 1
    elif before == 0:
        counting[1] += 1
    elif before == 1:
        counting[2] += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
counting = [0, 0, 0]

sepa(0, 0, N)
for i in range(3):
    print(counting[i])