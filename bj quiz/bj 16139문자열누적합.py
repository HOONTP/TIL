import sys
input = sys.stdin.readline
#pypy만 100점뜸
sen = input().strip()
arr = [[0]*200001 for _ in range(26)]
N = int(input())
M = len(sen)
for w in range(26):
    for i in range(M):
        nums = ord(sen[i])-97
        if nums == w:
            arr[w][i] = arr[w][i-1] + 1
        else:
            arr[w][i] = arr[w][i-1]
for _ in range(N):
    A, l, r = input().split()
    m = ord(A)-97
    result = arr[m][int(r)] - arr[m][int(l)-1]
    print(result)