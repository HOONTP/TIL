import sys
input = sys.stdin.readline

def repeat_de(n, m):
    if m == 0:
        return 1
    if (n,m) in repeat:
        return repeat[(n, m)]
    repeat[(n, m)] = (repeat_de(n-1, m-1) + repeat_de(n-1, m)) % 1000000007
    return

N, M = map(int, input().split())
repeat = {}
repeat_de(N, M)
print(repeat[(N, M)])

# result = 1
# for i in range(M):
#     result *= ((N-i)/(M-i))
#     if result > 1000000007:
#         result %= 1000000007
# print(result)