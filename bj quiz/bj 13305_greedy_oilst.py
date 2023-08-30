import sys
input = sys.stdin.readline

N = int(input())
#코드가 너무 복잡해진다아아아아아아아
distances = list(map(int, input().split()))
fees = list(map(int, input().split()))

sums = 0
i = 0
while i < N-1:# 순방향 역방향 음..
    if fees[i] >= fees[i+1]: # 현재가 더 크면 최소만. #현재가 작으면? 더작은게 나올때까지 채우기?
        sums += distances[i]*fees[i]
    elif fees[i] < fees[i+1]:
        restore = 0
        j = i + 1
        while True:
            if j == N-1:
                sums += restore + distances[j-1]*fees[i]
                i = j - 1
                break
            if fees[i] <= fees[j]:
                restore += distances[j-1]*fees[i]
            else:
                restore += distances[j - 1] * fees[i]
                sums += restore
                i = j - 1
                break
            j += 1
    i += 1
print(sums)

