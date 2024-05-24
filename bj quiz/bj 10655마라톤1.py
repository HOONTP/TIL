N = int(input())

checkList = []
for i in range(N):
    x, y = map(int, input().split())

    checkList.append((x, y))

distSum = [0]
maxSave = 0
for i in range(N-1):
    x1, y1 = checkList[i]
    x2, y2 = checkList[i + 1]
    if i < N-2:
        x3, y3 = checkList[i + 2]

        distOrigin = abs(x1 - x2) + abs(y1 - y2) + abs(x3 - x2) + abs(y3 - y2)
        distShort = abs(x1 - x3) + abs(y1 - y3)

        distSave = distOrigin - distShort
        if distSave > maxSave:
            maxSave = distSave

    dist = abs(x1 - x2) + abs(y1 - y2)
    distSum.append(dist+distSum[i])

print(distSum[-1] - maxSave)