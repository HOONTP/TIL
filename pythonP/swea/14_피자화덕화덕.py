from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    lst = deque(lst)
    fire = deque()
    i = 1

    while True:
        n = len(fire)
        if not lst and n == 1:
            break
        if n < N and lst:
            fire.append([lst.popleft(), i])
            i += 1
        else:
            chz = fire.popleft()
            if chz[0]//2 != 0:
                fire.append([chz[0]//2, chz[1]])
            else:
                pass
    print(f'#{tc}', fire[0][1])