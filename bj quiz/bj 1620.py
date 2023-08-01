import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pk_lst = []
num_lst = []
for _ in range(N):
    name = input().strip()
    pk_lst.append(name)
    num_lst.append(_)

set_p = set(pk_lst)
set_n = set(num_lst)

for i in range(M):
    quiz = input().strip()
    if quiz in set_p:
        idx = pk_lst.index(quiz) + 1
        print(idx)
    else:
        idx_ = int(quiz)-1
        print(pk_lst[idx_])