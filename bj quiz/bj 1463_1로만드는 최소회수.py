import sys
input = sys.stdin.readline

N = int(input())

dic_ = {}
dic_[0] = 0
dic_[1] = 0
for i in range(2, N+1):
    one = dic_[i-1] + 1
    if i % 2 == 0 and dic_[i//2] in dic_:
        two = dic_[i//2] + 1
    else:
        two = 100000
    if i % 3 == 0 and dic_[i//3] in dic_:
        three = dic_[i//3] + 1
    else:
        three = 1000000
    dic_[i] = min(one, two, three)

print(dic_[N])