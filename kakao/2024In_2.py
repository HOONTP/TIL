from collections import deque


def solution(edges):  # n -> n  n -> n - 1  n -> 2n+1 -> 2n+2 // n+1/2 -> n+1
    N = 0
    M = len(edges)
    for line in edges:
        if N < max(line):
            N = max(line)

    cntSet = set()
    connect = [[] for _ in range(N + 1)]
    reverse = [[] for _ in range(N + 1)]
    shoot = [0 for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]
    for line in edges:
        a, b = line
        connect[a].append(b)
        reverse[b].append(a)
        cntSet.add(a)
        cntSet.add(b)
        shoot[a] += 1
        shoot[b] -= 1
    n = len(cntSet)

    origin = shoot.index(max(shoot))
    indexList = connect[origin]
    result = [origin, 0, 0, 0]

    for i in indexList:
        q = deque()
        q.append(i)

        while q:
            node = q.popleft()

            tarSize = len(connect[node])
            if tarSize == 2:
                result[3] += 1
                q = [1]
                break

            if tarSize == 0:
                result[2] += 1
                q = [1]
                break

            for target in connect[node]:
                if visited[target] == 1: continue
                q.append(target)
                visited[target] = 1

        if len(q) == 0:
            result[1] += 1

    answer = result
    return answer