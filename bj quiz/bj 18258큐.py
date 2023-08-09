from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
que = []
my_que = deque(que)
for _ in range(N):
    A = list(input().split())

    if len(A)>1:
        my_que.append(A[-1])
    elif A[0] == 'pop':
        if my_que:
            print(my_que.popleft())
        else:
            print(-1)
    elif A[0] == 'size':
        print(len(my_que))
    elif A[0] == 'empty':
        if my_que:
            print(0)
        else:
            print(1)
    elif A[0] == 'front':
        if my_que:
            print(my_que[0])
        else:
            print(-1)
    elif A[0] == 'back':
        if my_que:
            print(my_que[-1])
        else:
            print(-1)