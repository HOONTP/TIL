import sys
input = sys.stdin.readline

N = int(input())
lst_o = list(map(int, input().split()))

set_lst = set(lst_o)
lst = sorted(set_lst)
dic_ = {}
M = len(set_lst)
i = M-1
for i in range(M):
    dic_[lst[i]] = i


for it in lst_o:
    print(dic_[it], end=' ')
