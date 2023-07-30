import sys
input = sys.stdin.readline

M = int(input())
N = int(input())
lst = []

for i in range(2,N+1):
    count = 0
    ic = 2
    while i > ic:
        if i % ic == 0:
            count +=1
            break
        ic += 1
    if count == 0:
        lst.append(i)


set_lst = set(lst)
sel_lst = []

for it in range(M, N+1):
    if it in set_lst:
        sel_lst.append(it)


if len(sel_lst) == 0:
    print('-1')
else:
    print(sum(sel_lst))
    print(min(sel_lst))