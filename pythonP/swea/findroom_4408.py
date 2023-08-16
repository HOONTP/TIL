T = int(input())

def check_origin(i,j):
    if j == len(lst):
        return
    if max(lst[i][0], lst[i][1]) < min(lst[j][0], lst[j][1]):
        nums.append(j)
        return check_origin(j, j+1)
    else:
        return check_origin(i, j+1)

for tc in range(1, T+1):
    N = int(input())
    lst = []
    for _ in range(N):
        A, B = map(int, input().split())
        if B < A:
            A, B = B, A
        lst.append([(A+1)//2, (B+1)//2])

    lst.sort()
    i = 0
    cnt = 0
    while len(lst) > 0:# 선택한 범위보다 두 값 모두 큰 경우
        nums = []
        nums.append(0)
        check_origin(0, 1)
        lst = [lst[k] for k in range(len(lst)) if k not in nums]
        cnt += 1

    print(f'#{tc}', cnt)

    # 하나를 선택 후 얘와 겹치지 않는 애를 선택 후 애와 겹치지 않는 쟤를 선택하는데~ 더이상 없다면 딜리트?
