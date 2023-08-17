T = 10

for tc in range(1, T+1):
    N = int(input())
    nums = input()

    stack = []
    i = 0
    while i < N:
        if nums[i] == '+':
            stack.append(stack.pop()+int(nums[i+1]))
            i += 2
        else:
            stack.append(int(nums[i]))
            i += 1
    print(f'#{tc}', stack[0])

'''
    N = int(input())
infix = input()
postfix = ''
stack = [0] * N
top = -1
icp = {'+': 1, '*': 2}  # 연산자 우선순위
for i in range(N):
    if '0' <= infix[i] <= '9':  # 피연산자인 경우
        postfix += infix[i]
    else:  # 연산자인 경우
        if top > -1 and icp[stack[top]] >= icp[infix[i]]:  # stack[top] 우선순위가 같거나 높으면  pop
            postfix += stack[top]
            top -= 1
        top += 1
        stack[top] = infix[i]
while top > -1:     # 남아있는 연산자를 수식뒤에 붙임
    postfix += stack[top]
    top -= 1
print(postfix)'''