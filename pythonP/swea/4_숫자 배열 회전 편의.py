# 제출은 못하지만 n 회 만큼 90도 회전하는 함수
# 2차원 배열은 함수에 넣더라도 내부가 주소를 공유해서 본체가 바껴버린다.

T = int(input())

def Rotate(arr, n): # 열,n-2 = n-2,행
    new_arr = [[0]*N for _ in range(N)]
    md_lst = [[0]*N for _ in range(N)]
    for k in range(N):
        for l in range(N):
            md_lst[k][l] = arr[k][l]
    for _ in range(n):
        for i in range(N):
            for j in range(N):
                new_arr[j][N-1-i] = md_lst[i][j]
        for k in range(N):
            for l in range(N):
                md_lst[k][l] = new_arr[k][l]
    return new_arr

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    rot_1 = Rotate(lst, 1)
    rot_2 = Rotate(lst, 2)
    rot_3 = Rotate(lst, 3)


    for i in range(N):
        print(*rot_1[i], *rot_2[i], *rot_3[i])
