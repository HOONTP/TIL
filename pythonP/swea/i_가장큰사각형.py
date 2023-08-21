T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx_lst = [0, 0]
    for i in range(N):
        for j in range(N):
            n = arr[i][j]
            if (N-i+1)*(N-j+1) < mx_lst[0]:
                continue
            for k in range(i, N):
                for l in range(j, N):
                    size = 0
                    if n == arr[k][l]:
                        size = (k-i+1)*(l-j+1)
                    if size > mx_lst[0]:
                        mx_lst = [size, 1]
                    elif size == mx_lst[0]:
                        mx_lst[1] += 1
    print(f'#{tc}', mx_lst[1])
'''
일단 크기를 구하려면 i, j가 활용되야함.
일단 완탐을 하는 방법
50 * 50 행렬에서 => 2500 칸
20 이하의 숫자를 탐색 (i, j)를 모두 확보한다음 2500을 20번 검토 50000 ok
2500개의 칸 20개씩이라치면 숫자 하나당 125개의 칸 => 각각 차이계산 126*65 => 8000천 * 20 ok?
차이가 가장 큰 것들의 개수만 저장한다.
하지만 노가다 너무 귀찮은데 .. ;
'''
'''
각 칸에서 만들 수 있는 최대크기의 사각형을 저장? 이게 더 시행이 많을 수도 있겠는데?
2500 * 1000은 되지 않을까 2500000
그럼 뭐가 더 간단하지?
'''