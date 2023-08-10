import sys
input = sys.stdin.readline

N = int(input())
set_ = set()
cnt = 0

for _ in range(N):
    name = input().strip()

    if name == 'ENTER':
        set_ = set()
    else:
        if name in set_:
            pass
        else:
            cnt += 1
            set_.add(name)
print(cnt)