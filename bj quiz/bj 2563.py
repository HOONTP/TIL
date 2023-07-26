import sys
input = sys.stdin.readline

N = int(input())

# grap = [[0 for _ in range(100)] for _ in range(100)]
grap = []
n = []
for NNN in range(100):
    m = []
    for NN in range(100):
        m.append(0)
    grap.append(m)

for NNNN in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for it in range(10):
            grap[x+i][y+it] = 1

Count = 0
for NTP in range(100):
    Count += grap[NTP].count(1)
print(Count)