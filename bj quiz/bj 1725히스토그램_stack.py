import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

stack = [[0, lst[0], 0]]
result = [0] * N
# print(lst)
i = N - 1 # 이게 필요한가
for i in range(1, N):
    if stack[-1][1] < lst[i]:
        stack.append([i, lst[i], i])
    elif stack[-1][1] == lst[i]:
        stack.append([stack[-1][0], lst[i], i])
    else:
        while stack:
            if stack[-1][1] > lst[i]:
                result[stack[-1][0]] = max(result[stack[-1][0]], stack[-1][1] * (i - stack[-1][0]))
                stack.pop()
            elif stack[-1][1] == lst[i]:
                stack.append([stack[-1][0], lst[i], i])
                break
            else:
                stack.append([stack[-1][2]+1, lst[i], i])
                break
        if not stack:
            stack.append([0, lst[i], i])
    # print(stack)

#남은걸 어떻게 하지?
while stack:
    result[stack[-1][0]] = max(result[stack[-1][0]], stack[-1][1] * (i - stack[-1][0] + 1))
    stack.pop()
# print(result)
print(max(result))
'''
스택에 담다가 [index, values] 작은 값이 나오면 pop하면서 값 저장 values * (now index - old index)하면 될듯?
'''
'''이게 거의 완전한 반례가 아닐까,, (내코드기준)
8
4
7
6
8
3
9
4
5
'''