while True:
    n=int(input())
    if n==0:
        break

    primes=set(range(2, 2*n+1))
    for i in range(2, int((2*n)**0.5)+1):
        if i in primes:
            primes-=set(range(2*i, 2*n+1, i))
    primes-=set(range(2, n+1))

    print(len(primes))