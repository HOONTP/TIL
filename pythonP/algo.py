import sys
input = sys.stdin.readline
from collections import deque
'''
해당되는 인덱스 모두 찾은 다음에 큐 / 스택 교차로 검증하면 되지 않을까?
중간에 발생한 애들은 어쩔?

담으면서 좌우로 비교하면 될거 같긴한데 큐가 list형식이라 문자열과 비교하려면 좀 어려울 듯 싶음.?
혹은 계속 담은거 M개 만큼을 체크해보는 방법도 괜찮고
'''

key = input().strip()
full = input().strip()
N = len(full)
M = len(key)
un_key = ''
for i in key:
    un_key = i + un_key

q = deque(full)
front = []
back = []
W = 'F' # or B

n = 0
m = N - 1
while q:
    # print(front)
    # print(q)
    # print(back)
    if W == 'F':
        while True:
            if key == ''.join(front[-M:]):
                for _ in range(M):
                    front.pop()
                for _ in range(M-1):
                    if front:
                        q.appendleft(front.pop())
                W = 'B'
                break
            else:
                if q:
                    front.append(q.popleft())
                else:
                    break
    else:
        while True:
            if un_key == ''.join(back[-M:]):
                for _ in range(M):
                    back.pop()
                for _ in range(M-1):
                    if back:
                        q.append(back.pop())
                W = 'F'
                break
            else:
                if q:
                    back.append(q.pop())
                else:
                    break
# print(front, 're')
# print(q)
# print(back)
while back:
    front.append(back.pop())
print(''.join(front))