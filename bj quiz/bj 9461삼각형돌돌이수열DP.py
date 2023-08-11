import sys

input = sys.stdin.readline

# n = n-2(-3 -7) n-3(-4 -8) 인데 왤까 n = n-1 ( -3 -4 ) n-5( -7 -8 ) (n = -3 -4 -7 -8)로 동일
def angle(n):
    dic_[1] = dic_[2] = dic_[3] = 1

    for w in range(4, n):
        dic_[w] = dic_[w - 2] + dic_[w - 3]


T = int(input())
dic_ = {}
angle(101)

for _ in range(T):
    N = int(input())
    print(dic_[N])