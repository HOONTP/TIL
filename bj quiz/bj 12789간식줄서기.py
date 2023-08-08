import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

wait_lst = []
get_num = 1
wait_num = N
n = N
while lst or wait_lst:
    if lst and lst[0] == get_num:#len(lst) 대신 lst 쓰며낻ㅁ
        lst.pop(0)
        get_num += 1
    elif wait_lst and wait_lst[-1] == get_num:
        wait_lst.pop()
        get_num += 1
    else:
        if lst:
            wait_lst.append(lst.pop(0))
        else:
            print('Sad')
            break

if len(lst) == 0 and len(wait_lst) == 0:
    print('Nice')