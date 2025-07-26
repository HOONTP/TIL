def solution(bandage, health, attacks):
    time = bandage[0]
    healing = bandage[1]
    clear = bandage[2]
    maxHP = health
    finish = attacks[-1][0]
    attackT = 0
    casting = 0
    for i in range(1, finish+1):
        if i == attacks[attackT][0]:
            casting = 0
            health -= attacks[attackT][1]
            attackT +=1
        else:
            health += bandage[1]
            casting += 1
            if casting == bandage[0]:
                health += bandage[2]
                casting = 0
            if health > maxHP:
                health = maxHP
            
        
        if health <= 0:
            break
            
    if health <= 0:
        answer = -1
    else:
        answer = health
    return answer