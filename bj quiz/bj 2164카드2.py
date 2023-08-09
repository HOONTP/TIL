from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

lst = []
que_lst = deque(lst)

for i in range(1,N+1):
    que_lst.append(i)

while True:
    if len(que_lst) == 1:
        break

    que_lst.popleft()
    if len(que_lst) == 1:
        break

    que_lst.append(que_lst.popleft())
print(que_lst[0])