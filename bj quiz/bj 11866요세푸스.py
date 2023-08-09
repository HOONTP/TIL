from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

lst = [i for i in range(1, N+1)]

result = []
que_lst = deque(lst)
i = 1
while que_lst:
    if i == K:
        result.append(que_lst.popleft())
        i = 1
    else:
        que_lst.append(que_lst.popleft())
        i += 1


print(f"<{', '.join(map(str, result))}>")