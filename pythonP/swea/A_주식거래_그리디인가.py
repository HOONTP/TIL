T = int(input())
'''
DP backt greedy


1. 전날과 비교하기
우선순위 : 퍼센트
+만 ? 담는다
순서는 ? 퍼센트도 같이 담아서 정렬
가능한 개수만큼 거래
남은 걸로 체크
2. 저축
'''
for tc in range(1, T+1):
    MS, MA = map(int, input().split())
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    seed = MS

    for day in range(1, L+1): # day
        percent = []
        for k in range(N): # 주식 수
            if arr[k][day-1] < arr[k][day]:
                percent.append((arr[k][day]/arr[k][day-1], k))
            percent.sort(reverse=True)
        if percent:
            sell = 0 # 매도 할 금액 축적
            for b in percent:
                if seed > arr[b[1]][day-1]:
                    buy = seed // arr[b[1]][day-1] # 구매 가능 개수
                    seed = seed % arr[b[1]][day-1] # 구매 하고 남은 금액
                    sell += buy*arr[b[1]][day] # 매도 하면 나올 금액 미리 저장
            seed = seed + sell
        seed += MA

    result = seed-MS-MA*L
    print(f'#{tc}', result)
