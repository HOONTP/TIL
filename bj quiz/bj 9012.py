import sys
input = sys.stdin.readline

N = int(input())

def PStr(PS):
    if len(PS)%2 == 1:
        return 'NO'
    
    c1, c2 = 0, 0

    c1 = PS.count('(')
    c2 = PS.count(')')
    
    if c1 != c2:
        return 'NO'
    
    count1 = 0
    count2= 0
    for i in PS:
        if i == ('('):
            count1 += 1
        elif i == (')'):
            count2 += 1
        if count2 > count1:
            return 'NO'
    return 'YES'

for _ in range(N):
    PS = input().rstrip() #/n 제거하기
    print(PStr(PS))

