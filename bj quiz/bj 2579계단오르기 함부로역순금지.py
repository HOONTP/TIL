import sys
input = sys.stdin.readline

def steps(k):
    for n in range(2, k+1):
        dic_[n, 'on', 'off'] = max(dic_[n-1, 'on', 'on'], dic_[n-1, 'off', 'on']) # 어차피 다음은 딛어야 하니까.
        dic_[n, 'off', 'on'] = dic_[n-1, 'on', 'off'] + lst[n-1]
        dic_[n, 'on', 'on'] = dic_[n-1, 'off', 'on'] + lst[n-1]

N = int(input())

lst = [int(input()) for _ in range(N)]
dic_ = {}
dic_[1, 'off', 'on'] = lst[0]
dic_[1, 'on', 'off'] = 0
dic_[1, 'on', 'on'] = lst[0]

steps(N)

print(dic_)

result = max(dic_[N, 'on', 'on'], dic_[N, 'off', 'on'])

print(result)

''' 역순으로 하면 편하지 않을까? 해서 역순으로 짯는데 오히려 더 복잡하고 개고생하고 답은 안나옴.
왜냐하면 마지막에 발을 딛는 경우만 고려해야 하는데. 역순으로하면 초기 값에 off를 넣을 수 밖에 없는데 마지막에 off가 들어간 값이 최대값이 되면 답이없다~이말
# def steps(n, before, now): 
#     if n == N-1:
#         dic_[n] = lst[n]
#     if before == 'on' and now == 'on':
#         return steps(n-1, 'on', 'off')
#     if before == 'on' and now == 'off':
#         return steps(n-1, 'off', 'on') + lst[n-1]
#     if before == 'off' and now == 'on':
#         return steps(n-1, 'on', 'on') + lst[n-1], steps(n-1, 'on', 'off')

# def steps(k, first, second):
#     for n in range(k-1, -1, -1):
#         if first == 'on' and second == 'on':
#             dic_[n-1, 'on', 'off'] = dic_[n, 'on', 'on']
#         if first == 'on' and second == 'off':
#             dic_[n-1, 'off', 'on'] = dic_[n, 'on', 'off'] + lst[n-1]
#         if first == 'off' and second == 'on':
#             dic_[n-1, 'on', 'off'] = dic_[n, 'off', 'on']
#             dic_[n-1, 'on', 'on'] = dic_[n, 'off', 'on'] + lst[n-1]

# def steps(k, first, second):
#     for n in range(k-1, 0, -1):
#         dic_[n, 'on', 'off'] = dic_[n+1, 'on', 'on']
#         dic_[n, 'on', 'off'] = dic_[n+1, 'off', 'on']
#         dic_[n, 'off', 'on'] = dic_[n+1, 'on', 'off'] + lst[n-1]
#         dic_[n, 'on', 'on'] = dic_[n+1, 'off', 'on'] + lst[n-1]
'''