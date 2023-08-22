T = 10

def cal(tre, n):
    s = n
    while s > 0:
        if tre[s] == '+':
            tre[s] = tre[c1[s]] + tre[c2[s]]
        elif tre[s] == '-':
            tre[s] = tre[c1[s]] - tre[c2[s]]
        elif tre[s] == '*':
            tre[s] = tre[c1[s]] * tre[c2[s]]
        elif tre[s] == '/':
            tre[s] = tre[c1[s]] / tre[c2[s]]
        s -= 1
    print(f'#{tc}', int(tre[1]))

for tc in range(1, T+1):
    N = int(input())
    c1 = [0] * (N + 1)
    c2 = [0] * (N + 1)
    tre = [0] * (N + 1)
    last = 0
    for _ in range(N):
        A = list(input().split())
        A[0] = int(A[0])
        if A[1].isdigit():
            tre[A[0]] = int(A[1])
        else:
            tre[A[0]] = A[1]
        if len(A) > 2:
            last = A[0]         #연산자의 마지막 인덱스
            c1[A[0]] = int(A[2])
            c2[A[0]] = int(A[3])

    cal(tre, last)