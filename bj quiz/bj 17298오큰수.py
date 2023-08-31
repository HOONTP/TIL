import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

# 100만개 100번 이내로 순회 해야되는데 ? 중 복 불 가 음  /  왕복?
'''
스택에 [인덱스, 해당 값]을 담는다.
'''
stack = [[0,lst[0]]]
result = [0 for _ in range(N)]

for i in range(1, N):
    if lst[i] <= stack[-1][1]: # lst[i]의 값이 담겨져있는 스택보다 작으면 계속 누적
        stack.append([i, lst[i]])
    if lst[i] > stack[-1][1]: # lst[i]의 값이 더 큰게 나오는 순간, 가능할때까지 stack에서 뽑아내면서 index에 lst[i]를 입력해준다.
        while stack and lst[i] > stack[-1][1]:
            result[stack[-1][0]] = lst[i]
            stack.pop()
        stack.append([i, lst[i]]) # 현재의 값이 이전 값보다 큰값으로 사용되었으니 스택에 담아줌
while stack:
    result[stack[-1][0]] = -1 # 스택에 남아있는 값에는 모두 -1을 부여
    stack.pop()
print(*result)