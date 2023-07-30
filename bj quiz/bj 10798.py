lst = []

for _ in range(5):
    st = input()
    lst.append(st)

for i in range(15):
    for it in range(5):
        try:
            print(lst[it][i], end = '')
        except IndexError:
            pass
