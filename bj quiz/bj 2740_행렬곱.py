import sys
input = sys.stdin.readline
'''
와 행렬 곱 원리 기억안나서 N.과 K.가 달라도 되는거 모르고 계속 제출 ㅡ.ㅡ;;
'''
N, M = map(int, input().split())

first = [list(map(int, input().strip().split())) for _ in range(N)]

M, K = map(int,input().split())

second = [list(map(int, input().strip().split())) for _ in range(M)]
pt = []
for i in range(N):
    result = []
    for j in range(K):
        mid = 0
        for k in range(M):
            mid += first[i][k]*second[k][j]
        result.append(mid)
    pt.append(result)

for _ in pt:
    print(*_)