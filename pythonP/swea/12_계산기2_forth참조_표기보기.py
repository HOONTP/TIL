T = 10

def infix(exp):#후위표기
    pre = {'+':1, '-':1, '*':2, '/':2}
    stack = []
    full = []

    for A in exp:
        if A.isalnum():
            full.append(A)
        elif A == '(':
            stack.append(A)
        elif A == ')':
            while stack and stack[-1] != '(':
                full.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and pre[A] <= pre.get(stack[-1], 0):
                full.append(stack.pop())
            stack.append(A)

    while stack:
        full.append(stack.pop())

    return ''.join(full)



for tc in range(1, T+1):
    N = int(input())
    exp = input()
    nums = infix(exp)
    # print(nums)

    result = 0
    stack = []
    
    for i in nums:#후위를 계산
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
