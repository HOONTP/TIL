T = int(input())

def fight(mid_lst):#처음엔 통째로 넣고
    # print(mid_lst)
    n = len(mid_lst)-1
    if n == 1:
        for i in range(2):
            if lst[mid_lst[i]] == '1' and lst[mid_lst[i+1]] == '2':
                return mid_lst[i+1]
            elif lst[mid_lst[i]] == '2' and lst[mid_lst[i+1]] == '3':
                return mid_lst[i+1]
            elif lst[mid_lst[i]] == '3' and lst[mid_lst[i+1]] == '1':
                return mid_lst[i+1]
            else:
                return mid_lst[i]
    elif n == 0:
        return mid_lst[0]


    A_lst = mid_lst[:n//2+1]
    B_lst = mid_lst[n//2+1:]
    # print(A_lst, B_lst)

    return fight([fight(A_lst), fight(B_lst)])#마지막에 2개중에 하나를 비교해야하니깐 나눠지는 걸 반복해서 나눠서 넣는다.




for tc in range(1, T+1):
    N = int(input())
    lst = list(input().split())
    ind = list(range(N))
    result = -1

    # print(lst)
    result = fight(ind) + 1
    print(f'#{tc}', result)