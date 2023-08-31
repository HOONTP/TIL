import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

# 100만개 100번 이내로 순회 해야되는데 ? 중 복 불 가 음  /  2회 순회?

stack = [[0,lst[0]]]
result = [0 for _ in range(N)]
counts = [0 for _ in range(1000001)] # 이것만 추가해서 코드짬

for i in lst:
    counts[i] += 1

for i in range(1, N):
    if counts[lst[i]] <= counts[stack[-1][1]]: # 비교 조건을 stack[1]과 lst[i] 에서 counts로 넘겨주기만했음.
        stack.append([i, lst[i]])
    if counts[lst[i]] > counts[stack[-1][1]]:
        while stack and counts[lst[i]] > counts[stack[-1][1]]:
            result[stack[-1][0]] = lst[i]
            stack.pop()
        stack.append([i, lst[i]])
while stack:
    result[stack[-1][0]] = -1
    stack.pop()
print(*result)