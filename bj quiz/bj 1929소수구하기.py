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

def find_prime(numa, numb):
    prime_lst = []
    for i in range(numa, numb+1):
        if is_prime(i):
            prime_lst.append(i)
    return prime_lst

M, N = map(int, input().split())

num_lst = find_prime(M, N)

for j in num_lst:
    print(j)