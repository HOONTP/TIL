T = int(input())

def tre(n):
    if c1[n] != 0:
        tre(c1[n])
    result.append(n)
    if c2[n] != 0:
        tre(c2[n])
'''
루트부터 1~N을 입력한후 좌측부터 순서대로 검토 => index가 들어있는 숫자가 됨. 
'''

for tc in range(1, T+1):
    N = int(input())
    c1 = [0] * (N + 1)
    c2 = [0] * (N + 1)
    name = [None] * (N+1)
    i = 1
    n = 2
    while n <= N: # 이렇게 직접 넣는게 맞나?
        c1[i] = n
        n += 1
        if n > N:
            break
        c2[i] = n
        n += 1
        i += 1
    '''
    for i in range(1,N+1): # 순서대로 입력 시, i 아래에는 i*2와 i*2+1이 붙는다.
    if i*2<=N:
        tree[i].append(i*2)
        ltree[i]=i*2
    if i*2+1<=N:
        tree[i].append(i*2+1)
        rtree[i]=i*2+1
    '''
    # print(c1)
    # print(c2)
    result = [0]
    tre(1)
    # print(result, 're')
    print(f'#{tc}', result.index(1), result.index(N//2))