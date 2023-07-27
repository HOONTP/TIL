import sys
input = sys.stdin.readline

N = int(input())
card_list = set(map(int, input().split()))

M = int(input())
num_list = list(map(int, input().split()))

for i in num_list:
    if i in card_list:
        print('1', end=' ')
    else:
        print('0', end=' ')