import sys
input = sys.stdin.readline

# def binary(n):
#     if n == 1
#     return binary(n-1) + binary(n-2)

# def binary(n): # dict는 너무 깊어져서 터질 수 있는듯?
#     if n <= 2: # DP는 무조건 N을 최대로해서 테스트 해볼 것
#         return dic_[n]
#     if n not in dic_:
#         dic_[n] = binary(n-1) + binary(n-2)
#     return dic_[n]

# def binary(lst, n): # 이거 할거면 굳이 함수 써야되나?
#     for i in range(3, N+1):
#         lst[i] = lst[i-1] + lst[i-2]
#     return lst[n]

N = int(input())

dic_ = {}
dic_[1] = 1
dic_[2] = 2
for i in range(3, N + 1):
    dic_[i] = (dic_[i - 1] + dic_[i - 2]) % 15746

print(dic_[N])