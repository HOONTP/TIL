N = int(input())
score = list(map(int, input().split()))
score.sort()

for i in range(N):
    score[i] = score[i]*100/score[N-1]

print(sum(score)/N)