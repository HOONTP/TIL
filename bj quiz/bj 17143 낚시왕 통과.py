import sys

# sys.stdin = open('input.in')
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]  # %4 쓰고 싶어서 순서 바꿔버림

R, C, M = map(int, input().split())
lst = []

for _ in range(M):  # ( r c s d z ) 행 열 속력 방향 크기
    shark = list(map(int, input().split()))
    lst.append(shark)

for X in lst:  # 방향 순서 바꾸기
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

    step_lst = [x for x in lst if x[1] == step]
    step_lst.sort()

    for i in step_lst:
        get += i[-1]
        i[:] = [0, 0, 0, 0, 0]
        break

    for j in lst:
        for k in range(4):
            if j[3] == k and j != [0,0,0,0,0]:
                j[0] += di[k]*j[2]
                j[1] += dj[k]*j[2]
                # print(j, '1')
                while True:
                    if 0 < j[0] <= R and 0 < j[1] <= C:
                        break
                    if j[0] < 1:
                        j[0] = 1 + (1 - j[0])
                        j[3] = (j[3] + 2) % 4
                    elif j[0] > R:
                        j[0] = R - (j[0] - R)
                        j[3] = (j[3] + 2) % 4
                    elif j[1] < 1:
                        j[1] = 1 + (1 - j[1])
                        j[3] = (j[3] + 2) % 4
                    elif j[1] > C:
                        j[1] = C - (j[1] - C)
                        j[3] = (j[3] + 2) % 4
                break # 이거 안써서 k == 1에서 돈 애가 3에서 또돌아서 오류났었음.

    # print(lst)

    check_lst = [[] for _ in range(R+1)]

    # print(lst)

    for l in range(M):
        for m in range(1,101):
            if lst[l][0] == m:#i좌표만 모으기.
                check_lst[m].append(lst[l])#lst[l]을 통째로 부여해서 주소공유
                break

    # print(check_lst)

    for n in range(1, R+1):#
        check_lst[n].sort(key=lambda x: x[4])
        for o in range(len(check_lst[n])):
            for p in range(o+1, len(check_lst[n])):
                if check_lst[n][o][1] == check_lst[n][p][1]:
                    check_lst[n][o][:] = [0, 0, 0, 0, 0]
                    break

    # print(check_lst)

    step += 1

print(get)