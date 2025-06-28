def solution(n, q, ans):
    answer = 0
    comb = []

    def dfs(start, depth):
        nonlocal answer
        if depth == 5:
            if is_valid(comb):
                answer += 1
            return

        for i in range(start, n+1):
            comb.append(i)
            dfs(i+1, depth+1)
            comb.pop()

    def is_valid(x):
        for i in range(len(q)):
            count = 0
            qi = q[i]
            
            for num in qi:
                if num in x:
                    count += 1
            
            if count != ans[i]:
                return False
        return True

    dfs(1, 0)
    
    return answer