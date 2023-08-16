T = int(input())

def fight(mid_lst):
    global result

    stack = []
    m = len(mid_lst)

    if m == 1:
        result = mid_lst[0] + 1
        return

    n = len(mid_lst)//2 # 까지 +1 부터
    i = 0

    while True:
        if m != 2 and i == n-1:
            stack.append(mid_lst[i])
            i += 1
            continue
        if i == m:
            fight(stack)
            break
        elif m != 2 and i == m-1:
            stack.append(mid_lst[i])
            fight(stack)
            break
        if lst[mid_lst[i]] == '1' and lst[mid_lst[i+1]] == '2':
            stack.append(mid_lst[i+1])
        elif lst[mid_lst[i]] == '2' and lst[mid_lst[i+1]] == '3':
            stack.append(mid_lst[i+1])
        elif lst[mid_lst[i]] == '3' and lst[mid_lst[i+1]] == '1':
            stack.append(mid_lst[i+1])
        else:
            stack.append(mid_lst[i])
        i += 2
    return

for tc in range(1, T+1):
    N = int(input())
    lst = list(input().split())
    mid_lst = list(range(N))
    result = -1

    fight(mid_lst)
    print(f'#{tc}', result)