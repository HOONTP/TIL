import sys
input = sys.stdin.readline

N = int(input())

lst = [1] * 10
lst[0] = 0
new_lst = [0] * 10
new_lst[:] = lst[:]#리스트 복사 주의 [:] 빼면 안된다.

for n in range(N-1):
    for i in range(10):
        if i == 0:
            new_lst[1] += lst[i]
            new_lst[i] -= lst[i]
        elif i == 9:
            new_lst[8] += lst[i]
            new_lst[i] -= lst[i]
        else:
            new_lst[i - 1] += lst[i]
            new_lst[i + 1] += lst[i]
            new_lst[i] -= lst[i]
    lst[:] = new_lst[:]
print(sum(new_lst)%1000000000)

    #본인은 빼야해 2개를 추가하는건 맞지만 횟수가 3배가 되버린다.