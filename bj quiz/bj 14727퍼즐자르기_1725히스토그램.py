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
for i in range(1, N): # ( 계산 ind, value, 찐 ind )
    if stack[-1][1] < lst[i]: # 현재의 값이 더 큰 경우 그냥 담는다. ( 본인이 최소 값이라 생각하기 때문에 현재 인덱스로 )
        stack.append([i, lst[i], i])
    elif stack[-1][1] == lst[i]:
        stack.append([stack[-1][0], lst[i], i]) # 같은 경우 스택의 마지막과 계산 ind를 맞춰준다.
    else: # 더 작은애가 나왔을 경우 작동
        while stack:
            if stack[-1][1] > lst[i]:  # 스택에 든 값이 더 큰경우 더 이상 이 케이스로 더 큰 크기의 직사각형을 만들 수 없기 때문에 계산처리
                result[stack[-1][0]] = max(result[stack[-1][0]], stack[-1][1] * (i - stack[-1][0]))
                stack.pop()
            elif stack[-1][1] == lst[i]: # 같을 경우 위의 elif문과 같이 처리 후 탈출
                stack.append([stack[-1][0], lst[i], i])
                break
            else: # 스택의 마지막 보다 큰 경우 == 더 작은 애를 만난 경우 / 더 작은애보다 다음칸부터 계산 가능하다
                stack.append([stack[-1][2]+1, lst[i], i]) # 이 경우 때문에 마지막에 찐index를 넣게되었다. 작은애의 계산인덱스는 이미 저 멀리 앞에 있기때문에 찐 index를 기준으로 계산 인덱스를 잡아야한다.
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