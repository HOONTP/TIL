def solution(cap, n, deliveries, pickups):  # 최대 탑재 50, 최대 거리 100000, 배달, 수거 [n]
    def work(lastpoint):
        power = cap
        delipoint = lastpoint
        pickpoint = lastpoint

        while power > 0:
            while deliveries[delipoint] == 0:
                delipoint -= 1
                if delipoint < 0:
                    break
            if delipoint < 0:
                break
            if power <= deliveries[delipoint]:
                deliveries[delipoint] -= power
                power = 0
            else:
                power -= deliveries[delipoint]
                deliveries[delipoint] = 0

        power = cap
        while power > 0:
            while pickups[pickpoint] == 0:
                pickpoint -= 1
                if pickpoint < 0:
                    break
            if pickpoint < 0:
                break
            if power <= pickups[pickpoint]:
                pickups[pickpoint] -= power
                power = 0
            else:
                power -= pickups[pickpoint]
                pickups[pickpoint] = 0
        return

    sums = 0
    i = n - 1
    while i >= 0:
        if deliveries[i] > 0 or pickups[i] > 0:
            count = work(i)
            sums += (i + 1) * 2
            # print(deliveries)
            # print(pickups)
        else:
            i -= 1
    # print(sums)
    return sums