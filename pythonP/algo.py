def bfs(A, B):
    q = []
    q.append((A, 0))
    visted[A] = 1

    while q:
        n = q.pop(0)
        if n[0] == B:
            print(f'#{t}', n[1])
            return
        cnt = n[1]+1
        if n[0]*2 <= B+10 and visted[n[0]*2] == 0:
            q.append((n[0]*2, cnt))
            visted[n[0]*2] = 1
        if n[0] > 10 and visted[n[0]-10] == 0:
            q.append((n[0] - 10, cnt))
            visted[n[0] - 10] = 1
        if n[0] > 1 and visted[n[0]-1] == 0:
            q.append((n[0] - 1, cnt))
            visted[(n[0] - 1)] = 1
        if n[0]+1 <= B+10 and visted[n[0]+1] == 0:
            q.append((n[0] + 1, cnt))
            visted[n[0] + 1] = 1

for t in range(1, int(input())+1):
    A, B = map(int, input().split())
    visted = [0] * (B + 11)
    bfs(A, B)