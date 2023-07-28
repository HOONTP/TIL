import sys
input = sys.stdin.readline

N, P, Q = list(map(int, input().split()))

def sigma(n, p, q):
    if n == 0:
        return 1    # 이거 안써서 여럿 제출
    if dic.get(n):  # 메모리즈로 최적화
        return dic[n]
    dic[n] = sigma(n//p, p, q) + sigma(n//q, p, q)
    return dic[n] 
    
dic = {}
result = sigma(N, P, Q)
print(result)


# 256 2 4

# 256 = 128        64

# 128 = 64 + 32    32 + 16

#     32 + 16 + 16 + 8 + 16 + 8 + 8 + 4

# 0이 몇개냐