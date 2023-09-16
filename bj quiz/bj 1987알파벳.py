import sys
input = sys.stdin.readline
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
dij = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# 이유는 모르나 python으로 돌리면 시간 초과.

def backT(n, visted, cnt):
    global max
    # 리스트에 담는 방법이 너무 메모리나 그런게 커서 파이썬에서는 오래 걸리고 파이파이는 잡아주는 방법이 있는 건가?
    if visted in max_lst[n[0]][n[1]]:# 해당 칸에 담겨있는 애들 중 동일한 수가 있으면 멈춤
        # print(visted)
        # print(max_lst)
        return
    else:
        max_lst[n[0]][n[1]].append(visted)

    for k in dij:
        ni = n[0] + k[0]
        nj = n[1] + k[1]
        if 0<= ni <R and 0<= nj <C and not num_lst[ni][nj] & visted:# ni,nj와 현재 visted를 비트로 비교
            visted += num_lst[ni][nj]
            backT((ni,nj), visted, cnt + 1)
            visted -= num_lst[ni][nj]
        else:
            if cnt == 26:
                print(cnt)
                exit()
            elif max < cnt:
                max = cnt

R, C = map(int, input().split())

arr = [input().strip() for _ in range(R)]
num_lst = [[0]*C for _ in range(R)]
max_lst = [[[] for _ in range(C)] for _ in range(R)]# 해당 위치에 오면서 담은 경로를 저장

for i in range(R):# arr을 비트 연산을 위해 숫자로 변환
    for j in range(C):
        for k in range(26):
            if arr[i][j] == uppercase_letters[k]:
                num_lst[i][j] = (1 << k)

# print(max_lst)
# print(num_lst)

max = 0

backT((0,0), num_lst[0][0], 1)
print(max)
# print(max_lst)
