import sys
input = sys.stdin.readline

def mini(n, visted): # 현재 노드랑 방문 리스트
    if memo[n][visted] != 0:
        return memo[n][visted]

    if visted == (1 << N) - 1:
        return arr[n][0] if arr[n][0] > 0 else float('inf')

    min_ = float('inf')

    for i in range(1, N):
        if not (visted & (1 << i)) and arr[n][i]: # 모든 노드를 방문하면서 데이터를 쌓는 것
            cost = mini(i, visted | (1 << i)) # 그 과정에서 지나온 경로의 합과 그 지점에서의 합을 구하는 건 이해 했음.
            min_ = min(min_, cost + arr[n][i]) # 아 ,,,,,,,,, 앞으로 갈 수 있는 노드는 정해져있으니 현재까지의 경로중 최소 값만 저장하면 되는 것?

    memo[n][visted] = min_
    return memo[n][visted]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

memo = [[0] * (1 << N) for _ in range(N)]
result = mini(0, 1)

print(result)
'''
각 지점에서 본인이 마지막이라 가정하고 계속해서 역 연산을 하면서 최소 값을 저장하는 방법  ? ? ? 
'''

