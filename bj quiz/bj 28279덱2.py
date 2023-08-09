from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
lst = []
que_lst = deque(lst)
for _ in range(N):
    rule = list(input().split())

    if rule[0] == '1':
        que_lst.appendleft(rule[-1])
    elif rule[0] == '2':
        que_lst.append(rule[-1])
    elif rule[0] == '3':
        if que_lst:
            print(que_lst.popleft())
        else:
            print(-1)
    elif rule[0] == '4':
        if que_lst:
            print(que_lst.pop())
        else:
            print(-1)
    elif rule[0] == '5':
        print(len(que_lst))
    elif rule[0] == '6':
        if que_lst:
            print(0)
        else:
            print(1)
    elif rule[0] == '7':
        if que_lst:
            print(que_lst[0])
        else:
            print(-1)
    elif rule[0] == '8':
        if que_lst:
            print(que_lst[-1])
        else:
            print(-1)