import sys

# sys.stdin = open('input.in')
input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    a = list(map(int, input().split()))
    if a[0] == 1:
        lst.append(a[1])
    elif a[0] == 2:
        if len(lst) >= 1:
            print(lst.pop())
        else:
            print('-1')
    elif a[0] == 3:
        print(len(lst))
    elif a[0] == 4:
        if len(lst) == 0:
            print('1')
        else:
            print('0')
    else:
        if len(lst) != 0:
            print(lst[-1])
        else:
            print('-1')