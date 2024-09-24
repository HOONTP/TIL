import sys
input = sys.stdin.readline

dict_ = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,     
    'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0, }
sum_score = 0.0
sum_size = 0.0
for _ in range(20):
    name, size, score = input().split()
    if score == 'P':
        continue
    sum_score += float(size) * dict_[score]
    sum_size += float(size)

print(sum_score/sum_size)
