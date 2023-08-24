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
def bfs(V, E):# 1개의 마을 기준으로 본인 일때 + 무언가 담아질때 계속해서 나머지와 분리 되는지 검토 가능?
    V.append(E.pop(0)) # 0 / 1 2 3 4

    while V:
        n = V.pop(0)
        for i in range(N):
            if arr[n][i] == 1:
                V.append(i)
                E.remove(i)
                bfs(V, E)
                check(E)
                V.pop()
                E.append(i)
    pass
# 아 부분집합이 훨씬 덜 헷갈리 겠는데 너무 하기 싫네에에에에에
for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = list(map(int, input().split()))
    print(arr)
    print(lst)

    visted = []
    other = list(range(N))
    chance = []

    bfs(visted, other)