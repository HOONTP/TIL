fix = [1, 1, 2, 2, 2, 8]

lists = list(map(int, input().split()))

dif = [fix[list_] - lists[list_] for list_ in range(6)]

[print(i, end=' ') for i in dif]