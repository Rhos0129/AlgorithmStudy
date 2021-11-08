m, n=int(input()), int(input())

primes=set(range(2, n+1))
for i in range(2, int(n**1/2)+1):
    if i in primes:
        primes-=set(range(2*i, n+1, i))
primes-=set(range(1, m))

if primes == set():
    print(-1)
else:
    print(sum(primes))
    print(min(primes))