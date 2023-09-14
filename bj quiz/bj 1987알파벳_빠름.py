import sys
input = sys.stdin.readline
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
dij = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def backT(n, visted, cnt):
    global max
    # 리스트로 도착 순간을 모두 저장하지 않으니 확실히 시간을 짧아졌음.
    # 너무 많이 거르려 하지말고 dfs니깐 동일한 순간만 걸러도 충분한듯?
    if visted == max_lst[n[0]][n[1]]:# 포함으로하면 안되고 동일 할 때만 멈춰야함.
        # print(visted)
        # print(max_lst)
        return
    else:
        max_lst[n[0]][n[1]] = visted

    # if visted & max_lst[n[0]][n[1]] == visted:# 해당 칸에 담겨있는 애들 중 동일한 수가 있으면 멈춤
    #     # print(visted)
    #     # print(max_lst)
    #     return
    # else:
    #     max_lst[n[0]][n[1]] = visted

    for k in dij:
        ni = n[0] + k[0]
        nj = n[1] + k[1]
        if 0<= ni <R and 0<= nj <C and not num_lst[ni][nj] & visted:# ni,nj와 현재 visted를 비트로 비교
            visted += num_lst[ni][nj]
            backT((ni, nj), visted, cnt + 1)
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
max_lst = [[0 for _ in range(C)] for _ in range(R)]# 해당 위치에 오면서 담은 경로를 저장

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
