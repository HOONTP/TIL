import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

# print(lst)
'''
스택에 담았다 치고 다음 i 에서 스택으로 역추적하면 나보다 큰넘이 나올때까지 계속 카운팅 해야함
'''
stack = []
cnt = 0
n = 0
for i in lst:
    j = -1
    if stack:
        equal = 0
        while -j <= n:
            # print(stack, j, n, i)
            if stack[j][0] < i:
                cnt += stack[j][1]
                stack.pop()
                n -= 1
            elif stack[j][0] == i:
                cnt += stack[j][1]
                stack[j][1] += 1
                j -= 1
                equal += 1
            else:
                if equal:
                    cnt += 1
                else:
                    cnt += 1
                    stack.append([i, 1])
                    n += 1
                break
    if not stack:
        stack.append([i, 1])
        n += 1
print(cnt)