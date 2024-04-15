from collections import deque
n, W, L = map(int, input().split())
dumpList = list(map(int, input().split()))
dumpListQueue = deque(dumpList)
q = deque([0 for _ in range(W)])
cnt = 0
while dumpListQueue or q:
    # print(dumpListQueue, cnt, q)
    if len(q) == W or len(dumpListQueue) == 0:
        q.popleft()

    if dumpListQueue:
        if sum(q) + dumpListQueue[0] <= L:
            q.append(dumpListQueue.popleft())
        else:
            q.append(0)
    cnt += 1
print(cnt)