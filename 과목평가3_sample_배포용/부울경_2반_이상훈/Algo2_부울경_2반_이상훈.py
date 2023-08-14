T = int(input())

for tc in range(1, T+1):
    nums = list(input())

    closed = [')', '}']
    opened = ['(', '{']
    stack = []
    mid_lst = []
    result = 0#사용할 변수들

    for i in nums:#문자열 순회
        if result == -1:#순회 중 탈출 조건
            break
        mid_lst = []#임시 저장소 초기화
        if i not in closed:#닫는게 아닌 경우
            if i in opened:#여는 경우
                stack.append(i)
            else:#숫자가 들어왔을 때 빈 스택을 고려하기 위한 조건
                if stack:
                    stack.append(i)
                else:
                    result = -1
                    break

        else:#닫는 괄호의 경우
            while True:
                if i == ')':
                    if stack:
                        if stack[-1] == '{':#짝이 안 맞다면 break
                            result = -1
                            break
                        elif stack[-1] == '(':#짝이 맞다면 임시저장소의 수 계산 후 stack에 저장
                            stack.pop()
                            plus = 0
                            if len(mid_lst) == 1:
                                stack.append(mid_lst[0])
                            elif len(mid_lst) == 0:
                                break
                            else:
                                for j in mid_lst:#()니까 더하기
                                    plus += j
                                stack.append(plus)
                            break
                        else:
                            mid_lst.append(int(stack.pop()))#정수형으로 변환 후 저장
                    else:#빈 스택 탈출
                        result = -1
                        break
                elif i == '}':
                    if stack:
                        if stack[-1] == '(':
                            result = -1
                            break
                        elif stack[-1] == '{':
                            stack.pop()
                            plus = 1
                            if len(mid_lst) == 1:
                                stack.append(mid_lst[0])
                            elif len(mid_lst) == 0:
                                break
                            else:
                                for j in mid_lst:#{}니깐 곱하기
                                    plus *= j
                                stack.append(plus)
                            break
                        else:
                            mid_lst.append(int(stack.pop()))
                    else:
                        result = -1
                        break
    if result == -1:
        print(f'#{tc}', result)
    elif len(stack) > 1:
        print(f'#{tc}', '-1')# ( 5 8 고려안했음 추가함.
    else:
        print(f'#{tc}', *stack)