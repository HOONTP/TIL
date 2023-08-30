import sys
input = sys.stdin.readline

sen = input().strip()
boom = input().strip()
n_count = len(boom)
stack = []
for i in sen:
    stack.append(i)
    if i == boom[-1]:
        if ''.join(stack[-n_count:]) == boom:# [index:] 에서는 index가 범위를 넘어도 ㄱㅊ 모두 추출
            for _ in range(n_count):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print("FRULA")
