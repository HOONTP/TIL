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
        else:#여기가 이해가 안가네.
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

'''표기법은 계싼기 1에
T = 10

for t in range(1, T+1):
    input()
    STR = input()

    STACK = []
    postfix = ''

    for s in STR:
        #숫자인경우 후위표기식에 추가
        if s.isdecimal():
            postfix += s
        else: #연산자 인경우
            while STACK and STACK[-1] == '*': #스택의 연산자가 *이면 높거나 같다
                postfix += STACK.pop()
            STACK.append(s) #현재 연산자를 스택에 추가

    while STACK:
        postfix += STACK.pop()

    result = []

    for p in postfix:
        if p.isdecimal():
            result.append(int(p))
        else:
            num2 = result.pop()
            num1 = result.pop()
            if p == '+':
                result.append(num1 + num2)
            elif p == '*':
                result.append(num1 * num2)


    print(f'#{t}', *result)
'''