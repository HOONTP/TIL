T = int(input())

def backt(A, now_A, i, SUM):
    global MIN

    if SUM > MIN:#SUM이 크면 나가리
        return
    if i == N:
        MIN = SUM # MIN보다 작은 SUM이 나오면 MIN교체 후 SUM은 result에 추가
        result.append(SUM)
        return

    for a in A:#[01234]순회
        if a not in now_A:#현재 중첩리스트에 없으면 시행
            now_A.append(a)#중첩 리스트에 넣고
            backt(A, now_A, i+1, SUM+arr[i][a])#a가 추가된 리스트, i -> i+1 다음 줄, SUM+현재 위치 값
            now_A.pop()#중첩리스트에 추가한a 제거해준 다음 다음 순회 시작

for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    A = [i for i in range(N)]

    MIN = 0
    result = []

    for i in range(N):#[01234] MIN 초기값으로
        MIN += arr[i][i]
    backt(A, [], 0, 0)#i=0 SUM=0으로 시작
    print(f'#{tc}', min(result))