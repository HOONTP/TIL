import sys
input = sys.stdin.readline

N = int(input())

dic_ = []
age_ = []
for NN in range(N):
    age, name = input().split()
    dic_.append({age:name})

for i in range(1,201):
    for it in range(N):
        key, value = list(dic_[it].items())[0]
        if int(key) == i:
            print(key, value)