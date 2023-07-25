import sys
input = sys.stdin.readline

N = int(input())

dic_ = []
age_ = []
for NN in range(N):
    age, name = input().split()
    age = int(age)
    i = 0
    try:
        while True:
            if age < age_[i]:
                dic_.insert(i, name)
                age_.insert(i, age)
                break
            elif age >= age_[i]:
                pass
            i += 1
    except IndexError:
        dic_.append(name) 
        age_.append(age)
for it in range(N):
    print(age_[it], dic_[it])
