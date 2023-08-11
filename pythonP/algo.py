import sys
input = sys.stdin.readline

def steps(n, before, now):
    if n == N-1:
        dic_[n] = lst[n]
    if before == 'on' and now == 'on':
        return steps(n-1, 'on', 'off')
    if before == 'on' and now == 'off':
        return steps(n-1, 'off', 'on') + lst[n-1]
    if before == 'off' and now == 'on':
        return steps(n-1, 'on', 'on') + lst[n-1], steps(n-1, 'on', 'off')

# def steps(n, first, second):
#     if n == N-1:
#         dic_[n, 'off', 'off', 'on'] = lst[n]
#         return
#     if first == 'on' and second == 'on':
#         dic_[n-1, 'on', 'on', 'off'] = dic_[n, 'off', 'off', 'on']
#     if first == 'on' and second == 'off':
#         dic_[n-1, 'on', 'off', 'on'] = dic_[n, 'off', 'off', 'on'] + lst[n-1]
#     if first == 'off' and second == 'on':
#         dic_[n-1, 'off', 'on', 'off'] = dic_[n, 'off', 'off', ''], steps(n-1, 'on', 'off')
#         dic_[n-1, 'off', 'on', 'on'] =

N = int(input())

lst = [int(input()) for _ in range(N)]
dic_ = {}
print(lst)

print(steps(N-1, 'off', 'on'))