import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

lst = [[0]*(N+1) for _ in range(N+1)]
'''
두 행렬의 크기를 맞추고 싶다면
# for i in range(N):
#     lst[i][0] = lst[i - 1][0] + arr[i][0]
# for j in range(N):
#     lst[0][j] = lst[0][j - 1] + arr[0][j]
'''
for i in range(1, N+1):#0을 한칸 채우는 방법으로 인덱스 고려
    for j in range(1, N+1):
        lst[i][j] = arr[i-1][j-1] + lst[i - 1][j] + lst[i][j - 1] - lst[i - 1][j - 1]
for _ in range(M):
    a,b,c,d = map(int, input().split())
    print(lst[c][d]-lst[c][b-1]-lst[a-1][d]+lst[a-1][b-1])#그림 그려서 인덱스 쓰기
