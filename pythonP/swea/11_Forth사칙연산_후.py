T = int(input())

for tc in range(1, T+1):
    nums = list(input().split())

    result = 0
    stack = []
    for i in nums:
        if i == '.':
            break
        if i in '*+-/':
            if len(stack) > 1:
                if i == '+':
                    stack.append(int(stack.pop())+int(stack.pop()))
                elif i == '*':
                    stack.append(int(stack.pop())*int(stack.pop()))
                elif i == '-':
                    stack.append(int(stack.pop(-2))-int(stack.pop()))
                else:
                    if stack[-1] != 0:
                        stack.append(int(stack.pop(-2))//int(stack.pop()))
                    else:
                        result = -1
                        break
            else:
                result = -1
                break
        else:
            stack.append(i)
    if result == 0:
        if len(stack) == 1:
            print(f'#{tc}', *stack)
        else:
            print(f'#{tc}', 'error')
    else:
        print(f'#{tc}', 'error')