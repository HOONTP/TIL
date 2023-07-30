lst = list(map(int, input().split()))

lst.sort()

while lst[2] >= lst[0] + lst[1]:
    lst[2] -= 1

print(sum(lst))