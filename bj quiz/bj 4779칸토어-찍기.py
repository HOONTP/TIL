import sys
input = sys.stdin.readline

def draw(lst):
    n = len(lst)//3
    if lst == ['-']:
        return print('-', end='')
    return draw(lst[:n]), print(' '*n, end=''), draw(lst[:n])


try:
    while True:
        N = int(input())
        lst = ['-']*(3**N)
        draw(lst)
        print()

except ValueError:
    pass