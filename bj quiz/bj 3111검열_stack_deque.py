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
'''
슬라이싱에 대해 여러가지 방법을 생각해봤지만 큐는 슬라이싱이 불가능 + 문자열은 기록을 보전하기가 힘듬
append를 받는 양 끝의 배열은 list로 받고 가운데서 자료를 주고 받는 역할을 하는 배열만 q로 지정.
'''
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
    if W == 'F':# 앞순서인지 뒷순서인지 판단
        while True:
            if key == ''.join(front[-M:]): # front에 계속 어펜드하면서 키가 완성되면 제거해주고 (M-1)개만큼 가능한한 되돌린다.
                for _ in range(M):
                    front.pop()
                for _ in range(M-1):
                    if front: # 되돌리는 데서 시간복잡도를 조금 걱정하긴 햇지만 키가 2배됐다고 생각하면 크지 않음.
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
            if un_key == ''.join(back[-M:]): # 앞과 마찬가지로 뒤도 같은 로직이다만 key를 뒤집어서 un_key를 사용했음.
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
while back: # q는 모두 소모됐고 back에 남아있는 것을 front로 옮겨줌.
    front.append(back.pop())
print(''.join(front))