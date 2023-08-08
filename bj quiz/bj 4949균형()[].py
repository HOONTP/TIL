while True:
    n = input()
    lst = []
    if n == '.':
        break
    for i in n:
        if i == '(':
            lst.append('1')
        elif i == '[':
            lst.append('2')
        elif i == ')':
            if len(lst) > 0 and lst[-1] == '1':
                lst.pop()
            else:
                print('no')
                lst.append(3)
                break
        elif i == ']':
            if len(lst) > 0 and lst[-1] == '2':
                lst.pop()
            else:
                print('no')
                lst.append(3)
                break
        elif i == '.':# 마지막 이 부분에서 길이에 따라 yes no를 출력 이부분 때문에 여러번 제출함.
            if len(lst) == 0:
                print('yes')
            else:
                print('no')
            break
