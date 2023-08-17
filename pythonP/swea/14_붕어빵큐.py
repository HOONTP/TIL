from collections import deque
T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    lst = list(map(int, input().split()))
    lst.sort()

    i = 0
    que = []
    que = deque(que)
    lst = deque(lst)
    result = 'Possible'

    while lst:
        if i != 0 and i % M == 0:
            for j in range(K):
                que.append(1)
        if i == lst[0]:
            if que:
                que.popleft()
                lst.popleft()
            else:
                result = 'Impossible'
                break
        i += 1
    print(f'#{tc}', result)
