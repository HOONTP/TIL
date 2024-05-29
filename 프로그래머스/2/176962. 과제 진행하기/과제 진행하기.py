from collections import deque

def diff(a, b): # 00:00
    aT = int(a[0]+a[1])
    aM = int(a[3]+a[4])
    
    bT = int(b[0]+b[1])
    bM = int(b[3]+b[4])
    
    dT = bT - aT
    dM = bM - aM
    
    dif = dT*60 + dM
    return dif

def solution(plans):
    q = deque()
    plans.sort(key=lambda x : x[1])
    answer = []
    
    for i in range(len(plans) - 1):
        time = diff(plans[i][1], plans[i+1][1])
        
        saveTime = time - int(plans[i][2])
        if saveTime < 0:
            q.append([plans[i][0], -saveTime])
        else:
            answer.append(plans[i][0])
            while q and saveTime >= int(q[-1][1]):
                name, time = q.pop()
                answer.append(name)
                saveTime -= time
            
            if q:
                q[-1][1] -= saveTime
    
    answer.append(plans[-1][0])
    
    while q:
        answer.append(q.pop()[0])
    
    
    return answer