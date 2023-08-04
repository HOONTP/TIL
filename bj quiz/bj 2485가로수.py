import sys
input = sys.stdin.readline

def gcd(i, b): # lst_minus를 호출하여 파라미터 i부터 그 안의 모든 lst의 최대 공약수
    if i == N-1 or i == 10:
        return b
    a = lst_minus[i]
    while b:
        a, b = b, a % b
    return gcd(i+1, a)

N = int(input())

lst = []

for _ in range(N):# 나무의 위치 리스트
    tr = int(input())
    lst.append(tr)

lst_minus = []# 각 나무의 사이 간격
for i in range(len(lst)-1):
    lst_minus.append(lst[i+1] - lst[i])

# lst_minus.sort() # 차이를 순서대로 정렬은 필요 없을지도
gcd_all = gcd(1, lst_minus[0]) # 모든 수의 최대 공약수

cnt = 0
for j in lst_minus:
    cnt += (j // gcd_all) - 1

print(cnt)