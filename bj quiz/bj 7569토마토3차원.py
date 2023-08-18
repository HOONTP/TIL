from collections import deque
import sys
input = sys.stdin.readline

#3차원을 2차원으로 풀면 진짜 노답되네
def bfs(tri, lst):
    q = deque()
    result = [0]#반례 조심하자. 한 번도 시행 안할 때 0 출력.
    for i in lst:
        q.append(i)

    while q:
        n = q.popleft()#h,i,j,cnt
        for k in range(6):
            nh = n[0] + dh[k]
            ni = n[1] + di[k]
            nj = n[2] + dj[k]
            if 0<=nh<H and 0<=ni<N and 0<=nj<M and tri[nh][ni][nj] == 0:#i인덱스 고려할것
                q.append([nh, ni, nj, n[3]+1])
                tri[nh][ni][nj] = 1
                result.append(n[3]+1)

    for i in tri:
        for j in i:
            if 0 in j:
                print(-1)
                return
    print(max(result))#만약 이렇게 안하고 max값을 갱신하는 형식으로 했다면 에러 안났을지도
    return


lst = []
tri = []

M, N, H = map(int, input().split())

di = [-1,0,1,0,0,0]#위아래로 번지는건 i를 N만큼 이동시킨다.
dj = [0,1,0,-1,0,0]
dh = [0,0,0,0,-1,1]

for _ in range(H):
    arr = [list(map(int,input().split())) for _ in range(N)]
    tri.append(arr)
        #인덱스에 리스트 하나만 담기게 하기 위해서.
for h in range(H):
    for i in range(N):#높이는 i인덱스에만 영향을 준다.
        for j in range(M):
            if tri[h][i][j] == 1:
                lst.append([h,i,j,0])

bfs(tri, lst)