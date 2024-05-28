import heapq

def solution(scoville, K):
    answer = 0
    q = []
    count = 0
    
    for num in scoville:
        heapq.heappush(q, num)
    
    while q[0] < K and len(q) != 1:
        
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        
        heapq.heappush(q, (a + b*2))
        count += 1
        
        

    if q[0] < K:
        return -1
    
    return count