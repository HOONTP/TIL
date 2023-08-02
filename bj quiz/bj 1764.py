import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst_n = set()
lst_m = set()
for _ in range(N):
    un_n = input().strip()
    lst_n.add(un_n)

for _ in range(M):
    un_m = input().strip()
    lst_m.add(un_m)

result = lst_n & lst_m

print(len(result))
result = sorted(result)
for i in result:
    print(i)