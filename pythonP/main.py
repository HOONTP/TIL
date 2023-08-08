T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    print(lst)
    restore = 0
    sell = 0
    for i in range(N):
