H, W, X, Y = map(int, input().split())
#2 4 1 1
totalMap = list(list(map(int, input().split())) for _ in range(H+X))


result = []
for i in range(H):
    if i < X:
        result.append(totalMap[i][:W])
    else:
        midResult = []
        for j in range(W):
            if j < Y:
                midResult.append(totalMap[i][j])
            else:
                midResult.append(totalMap[i][j] - result[i-X][j-Y])
        result.append(midResult)
for r in result:
    print(*r)