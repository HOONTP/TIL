import sys
# sys.stdin = open('input.in')
input = sys.stdin.readline

def find_num(num):
    while True:
        if is_num(num):
            return num
        num += 1

def is_num(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

T = int(input())

for _ in range(T):
    N = int(input())
    result = 0


    print(find_num(N))