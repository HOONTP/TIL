def solution(schedules, timelogs, startday):
    answer = 0
    checkDayList = []
    numCount = 6 - startday

    for i in range(0, 7):
        if numCount == 0 or numCount == -1:
            pass
        else:
            checkDayList.append(i)

        numCount -= 1

        if len(checkDayList) == 5:
            break

    j = 0

    n = len(schedules)
    for j in range(n):
        if isinstance(schedules, int):
            realTime = timeToMinute(schedules) + 10
        else:
            realTime = timeToMinute(schedules[j]) + 10

        TF = True
        for k in checkDayList:
            if isinstance(schedules, int):
                arrTime = timeToMinute(timelogs[k])
            else:
                arrTime = timeToMinute(timelogs[j][k])
            if arrTime > realTime:
                TF = False
                break

        if TF == True:
            answer += 1
    print(answer)
    return answer


def timeToMinute(num):  # str to int
    num = str(num)
    minute = num[-2:]
    hour = num[:-2]

    result = int(hour) * 60 + int(minute)
    return result