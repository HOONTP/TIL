import sys
input = sys.stdin.readline

sen = input().strip()
N = len(sen)

mid = ''
sums = 0
mid_sums = 0
for S in range(N-1, -1, -1):
    if sen[S].isdigit():
        mid = sen[S] + mid
    elif sen[S] == '+':
        mid_sums += int(mid)
        mid = ''
    elif sen[S] == '-':
        mid_sums += int(mid)
        mid = ''

        sums -= mid_sums
        mid_sums = 0
else:
    sums += int(mid)#제일 앞쪽 값은 무조건 +
sums += mid_sums# '-'를 만나지 못한 '+' 값
print(sums)

'''
깔끔한 코드
exp = input().split('-')
num = []
for i in exp:
    cnt = 0
    sum = i.split('+')
    for j in sum:
        cnt += int(j)
    num.append(cnt)
ans = num[0]
for i in range(1, len(num)):
    ans -= num[i]
print(ans)
'''