import sys
input = sys.stdin.readline

'''
20 명 중에 10명을 뽑고 능력치 계산 값 도출
이 문제 창의적으로 푼거 나중에 확인 해보자고오
'''

def backT(A, B, cnt):
    if cnt == N:
        sums_A = 0
        sums_B = 0
        for i in range(N//2):
            for j in range(N//2):
                sums_A += arr[A[i]][A[j]]
                sums_B += arr[B[i]][B[j]]

        result.append(abs(sums_A-sums_B))
        return
    if len(A) < N//2:
        A.append(cnt)
        backT(A, B, cnt+1)
        A.pop()
    if len(B) < N//2:
        B.append(cnt)
        backT(A, B, cnt+1)
        B.pop()

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

A = []
B = []
result = []
backT(A, B, 0)
print(min(result))