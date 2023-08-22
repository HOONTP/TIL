T = 10

def tre(n):
    if c1[n] != 0:
        tre(c1[n])
    result.append(name[n])
    if c2[n] != 0:
        tre(c2[n])
'''
완전 트리?라서 구지 간선 안 받아도
tre(n*2)
print(now)
tre(n*2+1)로 표현ㄱ ㅏ 능
'''
'''
중위순회
좌측 본인 우측 호출하면 계속해서 깊어지면서 좌측부터 순서대로 호출된다.
'''

for tc in range(1, T+1):
    N = int(input())
    c1 = [0] * (N + 1)
    c2 = [0] * (N + 1)
    name = [None] * (N+1)

    for _ in range(N):
        lst = input().split()
        n = int(lst[0])
        name[n] = lst[1]
        if len(lst) > 2:
            c1[n] = int(lst[2])
        if len(lst) > 3:
            c2[n] = int(lst[3])

    result = []
    tre(1)
    print(f'#{tc}', ''.join(result))