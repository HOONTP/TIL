import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    a, b = map(int, input().split())
    lst.append((a, b))

lst.sort()
# print(lst)
# if lst[i][1] <= lst[i+1][0]: # 어펜드 진행
#     pass
# else: # 어펜드 진행 <= 다음거 못받음 / 낫 어펜드 진행/ 백트나 디피로 가능한가
result = [lst[0]]
for i in range(1, N):
    if result[-1][1] > lst[i][1]:
        result.pop()
        result.append(lst[i])
    elif result[-1][1] <= lst[i][0]:
        result.append(lst[i])
# print(result)
print(len(result))