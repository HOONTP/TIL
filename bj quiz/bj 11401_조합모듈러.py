import sys
input = sys.stdin.readline

N, M = map(int, input().split())

top_value = 1
bottom_value = 1
mod_ = 1000000007
for i in range(M):
    top_value *= N - i
    top_value %= mod_
    bottom_value *= i + 1
    bottom_value %= mod_
# print(top_value)
# print(bottom_value)
result = top_value * pow(bottom_value, -1, mod_) % mod_ # 파이썬 버전이 pow에 영향이 있는 듯.
print(result)