T = int(input())
'''
무작위 2 분류로 쪼개서 모든 경우의수를 각각 탐색 가능한지 확인 후 합계 구하기?
'''
def check(e): # V는 A팀 B는 남은 팀
    #E팀이 다 돌아지는지?[2, 3, 4]
    q = [e[0]]
    v = []
    while q:
        n = q.pop(0)
        for i in range(N):
            if arr[n][i] == 1 and i not in v:
                q.append(i)
                v.append(i)
    if len(v) == len(e):
        print('yes')
    pass

def diff(E):
    total_vot = len(E)

    for i in range(1 << total_vot):
        A_group = []
        B_group = []

        for j in range(total_vot):
            if i & ( 1 << j ):
                A_group.append(E[j])
            else:
                B_group.append(E[j])

        if A_group and B_group:
            check(A_group)
            check(B_group)



# 아 부분집합이 훨씬 덜 헷갈리 겠는데 너무 하기 싫네에에에에에
for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = list(map(int, input().split()))

    all = list(range(N))
    chance = []

    diff(all)