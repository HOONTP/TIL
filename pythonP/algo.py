import sys
# sys.stdin = open('input.in')
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1] # %4 쓰고 싶어서 순서 바꿔버림

R, C, M = map(int, input().split())
lst = []

for _ in range(M):#( r c s d z ) 행 열 속력 방향 크기
    shark = list(map(int, input().split()))
    lst.append(shark)


for X in lst:# 방향 순서 바꾸기
    if X[3] == 1:
        X[3] = 0
    elif X[3] == 2:
        X[3] = 2
    elif X[3] == 3:
        X[3] = 1
    elif X[3] == 4:
        X[3] = 3

step = 1
get = 0

while step <= C:
    lst.sort()

    for i in lst:
        if i[1] == step:
            get += i[-1]
            i[:] = [0, 0, 0, 0, 0]
            break

    for j in lst:
        for k in range(4):
            if j[3] == k:
                for _ in range(j[2]):
                    if j[0] == 1 and j[3] == 0 or j[0] == R and j[3] == 2:
                        j[3] = (j[3] + 2) % 4
                        k = (k + 2) % 4
                    elif j[1] == 1 and j[3] == 3 or j[1] == C and j[3] == 1:
                        j[3] = (j[3] + 2) % 4
                        k = (k + 2) % 4
                    j[0] = j[0]+di[k]
                    j[1] = j[1]+dj[k]
                break

    for l in range(M):
        for m in range(l+1, M):
            if lst[l][0] == lst[m][0] and lst[l][1] == lst[m][1]:
                if lst[l][4] > lst[m][4]:
                    lst[m][:] = [0, 0, 0, 0, 0]
                else:
                    lst[l][:] = [0, 0, 0, 0, 0]

    step += 1

print(get)