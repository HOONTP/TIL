import sys
input = sys.stdin.readline
import pprint

def backT(arr,lst,n):
    if n == N:
        for ans in arr:
            print(*ans)
        sys.exit()#파괴는 찝찝해

    i, j = zero_lst[n]

    nine = []
    #이 파트를 미리 보관하면서 추가로 저장하는 방법을 사용하면 시간을 더 줄일 수 있을까?
    for a in range(i//3*3, i//3*3+3): # [0,1,2]=>(i//3) * 3 =>[0,3,6] +2개더
        for b in range(j//3*3, j//3*3+3):
            nine.append(arr[a][b])

    for num in range(1, 10):# 혹은 이 아래 부분을 set같은 것으로 보관하는 방법은?
        if num not in arr[i] and num not in lst[j] and num not in nine:
            arr[i][j] = num
            lst[j][i] = num
            backT(arr, lst, n+1)
            arr[i][j] = 0
            lst[j][i] = 0

arr = [list(map(int, input().split())) for _ in range(9)]
zero_lst = []
zipped = zip(*arr)
lst = [list(i) for i in zipped]

for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            zero_lst.append((i,j))

N = len(zero_lst)

# pprint.pprint(arr)
# pprint.pprint(lst)
# print(zero_lst)

backT(arr, lst, 0)


'''
012  012
345  012
678  012 .... 9가지 .. ? 너무 귀찮은데 ? ? ? ? ? ? ? ? ? ? ? ?
012  345
345  345 귀찮으면 방법이 있다...
'''