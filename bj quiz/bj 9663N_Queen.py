import sys
input = sys.stdin.readline

#python으로 제출하면 시간초과...
def backT(visted, angle, sums, i):
    global cnt
    global count
    count += 1
    if len(visted) == N:
        # print(visted)
        cnt += 1
        return
    #여기서 visted를 순회해서 대각선 비교 해야 하나?
    for j in range(1, N+1):
        if j not in visted and (i-j) not in angle and (i+j) not in sums:
            visted.append(j)
            angle.append(i-j)
            sums.append(i+j)
            backT(visted, angle, sums, i+1)
            visted.pop()
            angle.pop()
            sums.pop()

N = int(input())

visted = []
angle = []
sums = []
cnt = 0
count = 0
backT(visted, angle, sums, 0)
print(cnt)
print(count)

'''
대각선 i와j의 차이가 같으면
i가 같으면 같을 수 없음
j가 같으면 not in visted
but i,j 값이 입력되야 대각선도 구별 가능할듯?
이전과 같은지는 구분이 쉽지만
i가 아니라 차이값을 줘야 하나?
'''