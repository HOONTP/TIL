import sys
input = sys.stdin.readline

N = int(input())
lst = []
for i in range(2,10001):
    count = 0
    ic = 2
    while i > ic:
        if i % ic == 0:
                count += 1
        ic += 1
    if count == 0:
        lst.append(i)

num_lst = list(map(int, input().split()))
set_lst = set(lst)
cnt = 0 

for it in num_lst:
     if it in set_lst:
          cnt += 1

print(cnt)