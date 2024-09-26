import sys

input = sys.stdin.readline
# from collections import deque
# dij = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]

def rolling(number, direction):
    visited.add(number)
    left = number - 1
    right = number + 1
    newDirection = -direction
    if left not in visited and 0 <= left and chains[left][2] != chains[number][6]:
        rolling(left, newDirection)
    if right not in visited and right < 4 and chains[right][6] != chains[number][2]:
        rolling(right, newDirection)
    if direction == 1:
        chains[number] = chains[number][-1] + chains[number][:-1]
    else:
        chains[number] = chains[number][1:] + chains[number][0]

chains = []
for t in range(4):
    chains.append(input().replace("\n", ""))

K = int(input())
for k in range(K):
    num, direct = map(int, input().split())
    visited = set()
    rolling(num-1, direct)

result = 0
for i in range(4):
    result += int(chains[i][0])*(2**i)
print(result)