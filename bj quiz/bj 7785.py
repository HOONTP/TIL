import sys
input = sys.stdin.readline
N = int(input())

dic_ = {}
for _ in range(N):
    name, mode = input().split()
    dic_[name] = mode

result = []
for i in dic_:
    if dic_[i] == 'enter':
        result.append(i)

result.sort(reverse=True)

for it in result:
    print(it)
