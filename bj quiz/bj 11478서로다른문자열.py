import sys

# sys.stdin = open('input.in')
input = sys.stdin.readline

n= input().strip()
set_lst = set()

for i in range(len(n)):
    for j in range(i, len(n)):
        set_lst.add(n[i:j+1])

print(len(set_lst))