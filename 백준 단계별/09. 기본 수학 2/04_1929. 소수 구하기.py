m, n=map(int, input().split())

primes=set(range(2, n+1))
for i in range(2, int(n**1/2)+1):
    if i in primes:
        primes-=set(range(2*i, n+1, i))
primes-=set(range(2, m))

for i in sorted(primes):
    print(i)