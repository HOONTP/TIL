import sys
input = sys.stdin.readline

N = int(input())
lists = []
for _ in range(N):
    M = int(input())
    lists.append(M)

lists = lists[::-1]
count = 0
while True:
    if len(lists) == 1 or lists[N-1] > max(lists[:N-1]):
        break
    index_ = lists.index(max(lists[:N-1]))
    lists[index_] -= 1
    count += 1
    lists[N-1] += 1

print(count)