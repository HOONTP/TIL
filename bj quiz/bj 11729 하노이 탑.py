import sys
input = sys.stdin.readline
def draw(n, s, t, m):
    global cnt
    if n > 0:
        draw(n-1, s, m, t)
        cnt += 1
        result.append((s, t))
        draw(n-1, m, t, s)

N = int(input())
cnt = 0
result = []
draw(N, 1, 3, 2)
print(cnt)
for i in result:
    print(*i)

"""
1
1 -> 3 .1 
2
1 2 1이 1->2
1 3 1 새로운게 1-> 3
2 3 .2 1이 2->3
3
1 3 
1 2 
3 2  2가 1->2
1 3  새로운게 3으로가고
2 1  
2 3 
1 3  2가 2-> 3
4
1 2 
1 3 
2 3 
1 2 
3 1 
3 2 
1 2 
1 3 2 새로운 4가 1에서 3으로
2 3 2
2 1 3
3 1 .4
2 3 3
1 2 2
1 3 12
2 3 2

"""