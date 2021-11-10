t=int(input())
nums=[int(input()) for i in range(t)]

maxNum=max(nums)
primes=set(range(2, maxNum+1))
for i in range(2, int(maxNum**0.5)+1):
    if i in primes:
        primes-=set(range(2*i, maxNum+1, i))
primes=sorted(list(primes))

for num in nums:
    results=[]
    for prime in primes:
        if num-prime in primes:
            results.append((prime, num-prime))

    midIdx=int(len(results)/2)-1 if len(results)%2==0 else int(len(results)/2)
    print(results[midIdx][0], results[midIdx][1])
