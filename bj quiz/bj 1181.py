import sys
input = sys.stdin.readline

N = int(input())
lists = []
result = []
last_ = []
for i in range(N):
    S = input()
    S = S.strip()
    lists.append(S)

lists.sort()

for it in range(1, 51):
    for ic in lists:
        if len(ic) == it:
            result.append(ic)

last_ = [x for index, x in enumerate(result) if x not in result[:index]]

for fin in last_:
    print(fin)
