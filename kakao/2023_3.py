mxuser = 0
mxmoney = 0


def solution(users, emoticons):  # [n][2] / [m] / 백트래킹으로 4가지 케이스를 다 보내는 방향으로 7회반복 마지막에 계산?
    def backT(sales, n):
        global mxuser
        global mxmoney
        if n == M:
            count = 0
            money = 0
            for user in users:  # 100 * 7 * 16000
                mid_sum = 0
                for i in range(M):
                    if user[0] <= sales[i]:
                        mid_sum += (100 - sales[i]) * emoticons[i] // 100 # 이부분 앞쪽에 0.01 곱했더니 2테케 틀림.
                if user[1] <= mid_sum:
                    count += 1
                else:
                    money += mid_sum
            if mxuser < count:
                mxuser = count
                mxmoney = money
            elif mxuser == count and mxmoney < money:
                mxmoney = money
            else:
                pass
        else:
            for i in range(10, 41, 10):  # 일단 이러면 4**7개 만들어지긴함.
                sales.append(i)
                backT(sales, n + 1)
                sales.pop()
        return

    M = len(emoticons)
    backT([], 0)
    answer = [mxuser, mxmoney]

    return answer