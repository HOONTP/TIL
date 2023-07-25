all = []

for i in range(1, 29):
    A = int(input())
    all.append(A)

for ic in range(1, 31):
    if all.count(ic) > 0:
        continue
    else:
        print(ic)