import sys
# sys.stdin = open('input.in')
input = sys.stdin.readline

def is_prime(nums):
    if nums < 2:
        return False
    for i in range(2, int(nums**0.5)+1):
        if nums % i == 0:
            return False
    return True

def find_prime(num):
    prime_lst = []
    for i in range(num+1, 2*num+1):
        if is_prime(i):
            prime_lst.append(i)
    return prime_lst

while True:
    N = int(input())
    if N == 0:
        break
    num_lst = find_prime(N)
    print(len(num_lst))
