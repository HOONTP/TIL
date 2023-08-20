from collections import deque
import sys
input = sys.stdin.readline

'''
합의 모듈러 연산: (a + b) % c = ((a % c) + (b % c)) % c
차의 모듈러 연산: (a - b) % c = ((a % c) - (b % c)) % c
곱의 모듈러 연산: (a * b) % c = ((a % c) * (b % c)) % c
나눗셈의 모듈러 연산: (a / b) % c ≠ ((a % c) / (b % c)) % c (나눗셈의 경우 모듈러 성질이 성립하지 않음)
'''

def sqrt(A, B):
    # global cnt
    # cnt += 1
    if B < 3:
        return dict_[B]
    if B in dict_:
        return dict_[B]

    if B % 2 == 0:
        dict_[B] = (sqrt(A, (B // 2)) * sqrt(A, (B // 2))) % C
        return dict_[B]
    elif B % 2 == 1:# 5 2 2 1 9//2 4 4 1
        dict_[B] = (sqrt(A, (B // 2)) * sqrt(A, (B // 2)) * A) % C
        return dict_[B]


A, B, C = map(int, input().split())
dict_ = {}
dict_[0] = 1
dict_[1] = A
dict_[2] = A**2
# cnt = 0
print(sqrt(A, B) % C)
# print(cnt)