import sys
input = sys.stdin.readline

def backT(sums, num, four):
    if num == N-1:
        result.append(sums)
        return
    if four[0] > 0:
        four[0] -= 1
        backT(sums+lst[num+1], num+1, four)
        four[0] += 1
    if four[1] > 0:
        four[1] -= 1
        backT(sums-lst[num+1], num+1, four)
        four[1] += 1
    if four[2] > 0:
        four[2] -= 1
        backT(sums*lst[num+1], num+1, four)
        four[2] += 1
    if four[3] > 0:
        if sums >= 0:
            four[3] -= 1
            backT(sums//lst[num+1], num+1, four)
            four[3] += 1
        else:
            four[3] -= 1
            backT(-(-sums// lst[num + 1]), num + 1, four)
            four[3] += 1
    pass


N = int(input())

lst = list(map(int, input().split()))
four = list(map(int, input().split())) # + - * //

result = []
backT(lst[0], 0, four)
print(max(result))
print(min(result))

# print(-5//2) # -3 문제에서 원하는 것은 -2