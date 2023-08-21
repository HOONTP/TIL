import sys
input = sys.stdin.readline

def infix(exp):#후위표기
    pre = {'+':1, '-':1, '*':2, '/':2}
    stack = []
    full = []

    for A in exp:
        if A.isalnum():#문자열인가
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

exp = input().strip()

result = infix(exp)
print(result)