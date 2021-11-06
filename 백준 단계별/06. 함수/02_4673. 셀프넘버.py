def solve():

    def d(n):
        length=len(str(n))
        nums=[]; tmp=n
        for i in range(length-1, -1, -1):
            nums.append(tmp//(10**i))
            tmp%=(10**i)
        return n+sum(nums)

    lst=list(range(1, 10000))
    for i in range(10000):
        if d(i) in lst:
            lst.remove(d(i))

    for i in lst:
        print(i)

solve()