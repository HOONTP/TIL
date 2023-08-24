T = int(input())

for tc in range(1, T+1):
    MS, MA = map(int, input().split())
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)