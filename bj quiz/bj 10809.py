import string

S = input()
al = string.ascii_lowercase

for i in al:
    count = 0
    for ic in S:
        if ic != i:
            count += 1
        elif ic == i:
            print(count, end = ' ')
            break
    if ic != i:
        print('-1', end = ' ')