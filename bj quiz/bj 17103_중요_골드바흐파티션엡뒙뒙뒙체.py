import sys
# sys.stdin = open('input.in')
input = sys.stdin.readline

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):#p*(p)보다 작은 수의 배수는 이미 걸러졌다.
                is_prime[i] = False
        p += 1

    primes = [num for num in range(n + 1) if is_prime[num]]
    return primes


num_lst = sieve_of_eratosthenes(1000000)#미리 리스트 만들어놓기

T = int(input())#테케 개수를 주기 때문에 미리 최대값으로 리스트 생성해두자.

for _ in range(T):
    N = int(input())
    cnt = 0
    set_lst = set(num_lst)
    for i in num_lst:
        if i > N // 2:
            break
        if (N - i) in set_lst:
            cnt += 1
    print(cnt)