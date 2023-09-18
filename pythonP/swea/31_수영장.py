T = int(input())

for tc in range(1, T+1):
    price = list(map(int, input().split()))
    month = list(map(int, input().split()))
    DP = [0]*12

    mn = price[3]
    for i in range(12):
        day = DP[i-1] + price[0]*month[i]
        one = DP[i-1] + price[1]
        three = DP[i-3] + price[2]

        DP[i] = min(mn, day, one, three)
        if DP[i] == mn:
            DP[-1] = mn
            break
    print(f'#{tc}', DP[-1])