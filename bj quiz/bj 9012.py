import sys
input = sys.stdin.readline

N = int(input())

def PStr(PS):
    if len(PS)%2 == 0:
        return 'NO'
    
    c1, c2 = 0, 0

    c1 = PS.count('(')
    c2 = PS.count(')')
    
    if c1 != c2:
        return 'NO'
    
    lst = list(PS)
    lst_ = []
    for i in range(int((len(lst))/2)):
        lst_.append(lst[i])

    if lst_.count('(') >= lst_.count(')'):
        return 'YES'
    else:
        return 'NO'

for _ in range(N):
    PS = input()
    print(PStr(PS))

