def solution(video_len, pos, op_start, op_end, commands):
    mm, ss = map(int, pos.split(":"))
    endmm, endss = map(int, video_len.split(":"))
    opsmm, opsss = map(int, op_start.split(":"))
    opemm, opess = map(int, op_end.split(":"))
    
    endTot = endmm*60 + endss
    opsTot = opsmm*60 + opsss
    opeTot = opemm*60 + opess
    
    tot = mm*60 + ss

    for command in commands:
        if opsTot <= tot and tot <= opeTot:
            tot = opeTot
        tot = act(command, tot, endTot)

    
    if opsTot <= tot and tot <= opeTot:
        tot = opeTot
    
    answer = ''
    
    if tot//60 < 10:
        mm = "0" + str(tot//60)
    else:
        mm = str(tot//60)
    
    if tot%60 < 10:
        ss = "0" + str(tot%60)
    else:
        ss = str(tot%60)
    answer = mm + ":" + ss
    return answer

def act(X, tot, endTot):

    if X == "prev":
        tot -= 10
    elif X == "next":
        tot += 10
    
    if tot <= 0:
        tot = 0
    elif tot >= endTot:
        tot = endTot
        
    return tot
        