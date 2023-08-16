import sys
input = sys.stdin.readline
# import pprint

T = int(input())

for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    arr = [0]*N
    print(lst)
    print(arr)

    sums = 0
    result = 0
    cnt =0
    while len(lst)>1:
        i = lst.index(min(lst))
        cnt += 1
        if i == 0:
            sums = lst[i] + lst.pop(i+1)
            lst[i] = sums
            result += sums
            arr[i] += 1
            arr[i+1] += 1
        elif lst[i] == lst[-1]:
            sums = lst[i-1] + lst.pop()
            lst[i-1] = sums
            result += sums
            arr[i] += 1
            arr[i - 1] += 1
        elif lst[i-1] < lst[i+1]:
            sums = lst[i-1] + lst.pop(i)
            lst[i-1] = sums
            result += sums
            arr[i - 1] += 1
            arr[i + 1] += 1
        else:
            sums = lst[i] + lst.pop(i+1)
            lst[i] = sums
            result += sums
            arr[i] += 1
            arr[i + 1] += 1

    print(result, cnt)
    count = 0
    for i in range(2, N+1):
        count += i
    print(count)
    print(sum(arr))
# 40 30 50 30 35
# 40 30 / 70
# 40 30 30 / 40 60 / 100
# 40 30 30 10 / 40 30 40 / 40 70
# 40 + 70 + 110
# 60 + 70 + 110
#
# 20 10 5 5 100