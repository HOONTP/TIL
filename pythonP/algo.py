from collections import deque
import sys
input = sys.stdin.readline
'''
1번은 모두 표현 top / bottom / nothing 이게 그나마 직관적이고
    3가지 경우의 수를 모두 보내면 답은 나오지만 시행이 엄청 많다.
    """
    if cnt == N:
    print(sums)
    return
    
    DP(2, sums, (cnt+1))#선택 X

    if one == 0 or one == 2:
        DP(1, sums+arr[cnt][1], (cnt+1))

    if one == 1 or one == 2:
        DP(0, sums+arr[cnt][0], (cnt+1))
    """
시행이 왜 이렇게 오래걸리는거 같지?
'''

def DP(arr):#안 찎는 경우를 어떻게 고려할지 생각하기.

    re_up = [0]*100001#N이 1로 들어오는 경우도 생각해야함.
    re_down = [0]*100001
    re_up[0] = arr[0][0]
    re_down[0] = arr[0][1]
    for i in range(1, N):
        re_up[i] = max(re_down[i-1]+arr[i][0], re_down[i-2]+arr[i][0])
        re_down[i] = max(re_up[i-1]+arr[i][1], re_up[i-2]+arr[i][1])
    return max(re_up[N-1], re_down[N-1], re_up[N-2], re_down[N-2])

T = int(input())

for _ in range(T):
    N = int(input())

    arr = [[] for _ in range(N)]
    for _ in range(2):
        lst = list(map(int, input().split()))
        for i in range(N):
            arr[i].append(lst[i])

    result = DP(arr)
    print(result)