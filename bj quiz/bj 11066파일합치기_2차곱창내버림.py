import sys
input = sys.stdin.readline
# import pprint

T = int(input())

for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    result = [0]*N
    mid = [0]*N
    print(lst)

    mid[0] = result[0] = lst[0]
    mid[1] = result[1] = lst[0]+lst[1]

    for i in range(2, N):
        result[i] = min((result[i-1] + mid[i-1] + lst[i]), (result[i-2] + mid[i-2] + 2*(lst[i-1]+lst[i])))
        mid[i] = mid[i-1] + lst[i]

    print(mid, 'md')
    print(result, 're')


    # 7 12 22 34
    # 19 41 75