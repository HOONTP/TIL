import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()

num_lst = [0]*8001
mx_val = -4001
result = []

for i in lst:#모든 수 리스트에 인덱스에 맞춰서 저장 복잡도 N
    num_lst[i] += 1

# print(num_lst)

for i in range(8001):#최빈수(리스트의 최고값) 구하고 동점일 경우 저장
    if num_lst[i] > mx_val:
        result = [i]#동점이 아니면 통째로 교체
        mx_val = num_lst[i]
    elif num_lst[i] == mx_val:
        result.append(i)

# print(result)

for j in range(len(result)):
    if result[j] > 4000:#4001부터는 -4000이기때문에 빼기해주기
        result[j] = result[j] - 8001

# print(result)

result.sort()

print(round(max(lst)/N))
print(lst[N//2])

if len(result) > 1:
    print(result[1])
else:
    print(result[0])


print(lst[-1]-lst[0])
