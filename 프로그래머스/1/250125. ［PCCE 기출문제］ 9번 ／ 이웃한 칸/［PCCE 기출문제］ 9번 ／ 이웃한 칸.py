dij = [(-1,0), (0, 1), (1, 0), (0, -1)]
def solution(board, h, w):
    center = board[h][w]
    n = len(board)
    cnt = 0
    for i, j in dij:
        if 0<= h+i < n and 0 <= w+j < n and board[h+i][w+j] == center:
            cnt += 1
    
    answer = cnt
    return answer