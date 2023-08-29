import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9) #그냥 이런식으로 깊이를 넓히는게 어딧냐고;

def find(x):
    if dic_[x] != x:
        dic_[x] = find(dic_[x])
    return dic_[x]
N, M = map(int, input().split())

dic_ = {}
for i in range(N+1):
    dic_[i] = i

for _ in range(M):
    C, a, b = map(int, input().split())

    if C == 0:
        A = find(a)
        B = find(b)
        if A != B:
            dic_[A] = B
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")

#집합으로 만들어나 봤음
#     if C == 0:
#         lst[a] = lst[a] | lst[b]
#         lst[b] = lst[a]
#     else:
#         if a in lst[b]:
#             print("YES")
#         else:
#             print("NO")
# print(lst)