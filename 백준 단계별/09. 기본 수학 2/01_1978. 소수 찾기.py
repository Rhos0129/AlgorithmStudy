n=int(input())
nums=set(map(int, input().split()))

primes=set(range(2, max(nums)+1))
for i in range(2, int(max(nums)**1/2)+1):
    if i in primes:
        primes-=set(range(2*i, max(nums)+1, i))

print(len(nums&primes))


