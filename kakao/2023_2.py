def solution(cap, n, deliveries, pickups): # 최대 탑재 50, 최대 거리 100000, 배달, 수거 [n]
    for i in range(n-1,0,-1):
        deliveries[i-1] += deliveries[i]
        pickups[i-1] += pickups[i]
    # print(deliveries, pickups)
    count = 0
    sums = 0
    for i in range(n-1,-1,-1):
        clear = count * cap
        max_value = max(deliveries[i], pickups[i])
        if max_value > clear:
            num = (max_value - clear - 0.1) // cap + 1
            count += num
            sums += num*(i+1)*2
    return sums