N = input()

char = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in char:
    N = N.replace(i, 'A')

print(len(N))